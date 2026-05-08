from django import forms
from .models import Prediction, Driver


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['pole_driver', 'p1_driver', 'p2_driver', 'p3_driver']
        labels = {
            'pole_driver': 'Pole Position',
            'p1_driver': '1st Place',
            'p2_driver': '2nd Place',
            'p3_driver': '3rd Place',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        drivers = Driver.objects.all()
        for field_name in self.fields:
            self.fields[field_name].queryset = drivers
            self.fields[field_name].widget.attrs['class'] = 'form-select'