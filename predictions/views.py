from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.models import User

from .forms import PredictionForm, UserProfileForm
from .models import Race, Prediction
from .services import (
    get_user_stats,
    get_league_position,
    get_league_standings,
    get_upcoming_status,
    save_prediction,
    get_or_create_profile,
)


def race_list(request):
    """
    Display all races split into upcoming and past.
    Shows which races the user has already predicted (for button logic).
    """
    now = timezone.now()
    upcoming_races = Race.objects.filter(date__gte=now.date())
    past_races = Race.objects.filter(date__lt=now.date())

    # Get IDs of races the logged-in user has already predicted, so the
    # template can show "Edit Prediction" instead of "Make Prediction"
    predicted_race_ids = set()
    if request.user.is_authenticated:
        predicted_race_ids = set(
            Prediction.objects.filter(
                user=request.user, race__in=upcoming_races
            ).values_list('race_id', flat=True)
        )

    return render(request, 'predictions/race_list.html', {
        'upcoming_races': upcoming_races,
        'past_races': past_races,
        'predicted_race_ids': predicted_race_ids,
    })


@login_required
def race_detail(request, slug):
    """
    Show race details and prediction form for the logged-in user.
    Handles both new submissions and edits before the deadline.
    Locks the form after the prediction deadline.
    """
    race = get_object_or_404(Race, slug=slug)
    prediction = Prediction.objects.filter(
        user=request.user, race=race
    ).select_related(
        'pole_driver', 'p1_driver', 'p2_driver', 'p3_driver'
    ).first()
    deadline_passed = timezone.now() > race.prediction_deadline

    if request.method == 'POST':
        if deadline_passed:
            messages.error(
                request, 'The prediction deadline has passed.'
            )
            return redirect('race_detail', slug=slug)

        # ModelForm handles instance=None (creates new)
        # or existing instance (updates)
        form = PredictionForm(request.POST, instance=prediction)
        if form.is_valid():
            save_prediction(request.user, race, form)
            messages.success(request, 'Prediction submitted successfully!')
            return redirect('race_detail', slug=slug)
    else:
        form = PredictionForm(instance=prediction)

    return render(request, 'predictions/race_detail.html', {
        'race': race,
        'form': form,
        'prediction': prediction,
        'deadline_passed': deadline_passed,
    })


def leaderboard(request):
    """
    Display the league leaderboard with usernames and scores.
    """
    standings = get_league_standings()

    # Look up usernames for the user IDs in one query
    user_map = dict(
        User.objects.filter(id__in=[uid for uid, _ in standings])
        .values_list('id', 'username')
    )

    # Build (username, score) list for the template
    display_standings = [
        (user_map.get(uid, 'Unknown'), score) for uid, score in standings
    ]

    return render(request, 'predictions/leaderboard.html', {
        'standings': display_standings,
    })


@login_required
def profile(request):
    """
    Display the user's personal dashboard (My Garage):
    - Stats, league position, upcoming races, prediction history.
    Ensures a profile exists for the user.
    """
    user_profile = get_or_create_profile(request.user)

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
        # Unpacks: total_predictions, total_score,
        # correct_picks, total_picks, history
        **stats,
    })


@login_required
def edit_profile(request):
    """
    Allow the user to edit their profile
    (display name, favourite team, favourite driver).
    Ensures a profile exists even on first visit.
    """
    user_profile = get_or_create_profile(request.user)

    if request.method == 'POST':
        # User submitted the form — bind POST data to the
        # existing profile instance
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Profile updated successfully!'
            )
            # Redirect back to the dashboard so they see their changes
            return redirect('profile')
    else:
        # GET request — show the form pre-filled with their current data
        form = UserProfileForm(instance=user_profile)

    return render(request, 'predictions/edit_profile.html', {
        'form': form,
    })
