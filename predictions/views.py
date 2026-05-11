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
    """
    Shows the user's dashboard ("My Garage").
    - If the user doesn't have a UserProfile yet, it is created automatically.
    - Loads the profile and passes it to the template for display/editing.
    """
    # Get or create the user's profile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Render the dashboard template, passing the profile object
    return render(request, 'predictions/profile.html', {
        'user_profile': user_profile,
    })
