from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PredictionForm
from .models import Race, Prediction


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
