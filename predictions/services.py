"""
Service layer for the predictions app.

Keeps business logic out of views. Views call these functions to get
the data they need to render templates.
"""
from .models import Prediction, Race


def save_prediction(user, race, form):
    """
    Save a validated PredictionForm, attaching the given user and race.

    Returns the saved Prediction instance.
    """
    prediction = form.save(commit=False)
    prediction.user = user
    prediction.race = race
    prediction.save()
    return prediction


def get_user_stats(user):
    """
    Calculate stats for a user's completed predictions.

    Returns a dict with:
    - total_predictions: total number of predictions the user has made
    - total_score: sum of points across all completed races
    - correct_picks: number of individual driver picks that matched results
    - total_picks: total possible picks across completed races (4 per race)
    - history: list of {prediction, result, score} dicts for the dashboard
    """
    # Pre-load related objects to avoid extra database queries in the loop
    all_predictions = Prediction.objects.filter(user=user).select_related(
        'race', 'race__result',
        'pole_driver', 'p1_driver', 'p2_driver', 'p3_driver'
    )
    completed = all_predictions.filter(race__is_completed=True)

    total_score = 0
    correct_picks = 0
    history = []

    for prediction in completed:
        score = prediction.calculate_score()
        total_score += score
        result = prediction.race.result

        # Calculate points per position (5/10/5/3) — used in the template
        pole_pts = 5 if prediction.pole_driver_id == result.pole_driver_id else 0
        p1_pts = 10 if prediction.p1_driver_id == result.p1_driver_id else 0
        p2_pts = 5 if prediction.p2_driver_id == result.p2_driver_id else 0
        p3_pts = 3 if prediction.p3_driver_id == result.p3_driver_id else 0

        # Count correct picks (any position scoring > 0 means a correct pick)
        correct_picks += sum(1 for pts in [pole_pts, p1_pts, p2_pts, p3_pts] if pts > 0)

        history.append({
            'prediction': prediction,
            'result': result,
            'score': score,
            'pole_pts': pole_pts,
            'p1_pts': p1_pts,
            'p2_pts': p2_pts,
            'p3_pts': p3_pts,
        })

    return {
        'total_predictions': all_predictions.count(),
        'total_score': total_score,
        'correct_picks': correct_picks,
        'total_picks': completed.count() * 4,
        'history': history,
    }


def get_league_standings():
    """
    Build the leaderboard standings for all completed races.

    Returns a sorted list of (user_id, score) tuples, highest score first.
    """
    completed_races = Race.objects.filter(is_completed=True)
    preds = Prediction.objects.filter(
        race__in=completed_races
    ).select_related('user', 'race', 'race__result')

    scores = {}
    for pred in preds:
        scores[pred.user_id] = scores.get(pred.user_id, 0) + pred.calculate_score()

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def get_league_position(user):
    """
    Find a user's rank in the leaderboard.

    Returns (rank, total_players). Rank is None if the user has no scored
    predictions yet.
    """
    standings = get_league_standings()
    for i, (user_id, _) in enumerate(standings, 1):
        if user_id == user.id:
            return i, len(standings)
    return None, len(standings)


def get_upcoming_status(user, now):
    """
    Build a list of upcoming races with the user's submission status.

    `now` should be the current time (passed in so views can capture it once).
    Returns a list of dicts: {race, submitted, deadline_passed}.
    """
    upcoming_races = Race.objects.filter(date__gte=now.date())

    # Get IDs of races the user has predicted in a single query
    user_prediction_race_ids = set(
        Prediction.objects.filter(user=user, race__in=upcoming_races)
        .values_list('race_id', flat=True)
    )

    return [
        {
            'race': race,
            'submitted': race.id in user_prediction_race_ids,
            'deadline_passed': now > race.prediction_deadline,
        }
        for race in upcoming_races
    ]
