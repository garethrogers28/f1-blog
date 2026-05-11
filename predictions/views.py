from .services import get_user_stats, get_league_position, get_upcoming_status

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PredictionForm, UserProfileForm
from .models import Race, Prediction, UserProfile

def race_list(request):
    upcoming_races = Race.objects.filter(date__gte=timezone.now().date())
    past_races = Race.objects.filter(date__lt=timezone.now().date())
    return render(request, 'predictions/race_list.html', {
        'upcoming_races': upcoming_races,
        'past_races': past_races,
    })


@login_required
def race_detail(request, slug):
    race = get_object_or_404(Race, slug=slug)
    prediction = Prediction.objects.filter(user=request.user, race=race).first()
    deadline_passed = timezone.now() > race.prediction_deadline

    if request.method == 'POST':
        if deadline_passed:
            messages.error(request, 'The prediction deadline has passed.')
            return redirect('race_detail', slug=slug)

        if prediction:
            form = PredictionForm(request.POST, instance=prediction)
        else:
            form = PredictionForm(request.POST)

        if form.is_valid():
            pred = form.save(commit=False)
            pred.user = request.user
            pred.race = race
            pred.save()
            messages.success(request, 'Prediction submitted successfully!')
            return redirect('race_detail', slug=slug)
    else:
        if prediction:
            form = PredictionForm(instance=prediction)
        else:
            form = PredictionForm()

    return render(request, 'predictions/race_detail.html', {
        'race': race,
        'form': form,
        'prediction': prediction,
        'deadline_passed': deadline_passed,
    })

def leaderboard(request):
    completed_races = Race.objects.filter(is_completed=True)
    predictions = Prediction.objects.filter(race__in=completed_races).select_related('user', 'race')

    user_scores = {}
    for prediction in predictions:
        username = prediction.user.username
        score = prediction.calculate_score()
        if username not in user_scores:
            user_scores[username] = 0
        user_scores[username] += score

    standings = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)

    return render(request, 'predictions/leaderboard.html', {
        'standings': standings,
    })

@login_required
def profile(request):
    """Coordinates dashboard data and renders the template."""
    # Ensure profile exists
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    # Capture timezone.now() once for consistency across this request
    now = timezone.now()

    # Get stats from the service layer
    stats = get_user_stats(request.user)
    league_position, total_players = get_league_position(request.user)
    upcoming_status = get_upcoming_status(request.user, now)

    return render(request, 'predictions/profile.html', {
        'user_profile': user_profile,
        'league_position': league_position,
        'total_players': total_players,
        'upcoming_status': upcoming_status,
        # Unpacks: total_predictions, total_score, correct_picks, total_picks, history
        **stats,
    })


@login_required
def edit_profile(request):
    """
    Allows the logged-in user to edit their profile (display name, favourite team, favourite driver).
    - Uses get_or_create so a profile exists even if it's the user's first visit.
    - On POST: validates and saves the form, then redirects back to the dashboard with a success message.
    - On GET: shows the form pre-filled with the user's current profile data.
    """
    # Get or create the user's profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # User submitted the form — bind POST data to the existing profile instance
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            # Redirect back to the dashboard so they see their changes
            return redirect('profile')
    else:
        # GET request — show the form pre-filled with their current data
        form = UserProfileForm(instance=user_profile)

    return render(request, 'predictions/edit_profile.html', {
        'form': form,
    })