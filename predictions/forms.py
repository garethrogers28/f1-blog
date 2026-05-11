from django import forms
from .models import Prediction, Driver, UserProfile


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

    def clean(self):
        # Run the parent clean to get the cleaned_data dict
        cleaned_data = super().clean()

        # Collect podium picks (pole can still match the winner, that's normal)
        podium = [
            cleaned_data.get('p1_driver'),
            cleaned_data.get('p2_driver'),
            cleaned_data.get('p3_driver'),
        ]

        # Filter out any None values (in case a field is missing)
        filled = [driver for driver in podium if driver is not None]

        # If we have duplicates, the set will be shorter than the list
        if len(set(filled)) != len(filled):
            raise forms.ValidationError(
                "1st, 2nd and 3rd place must all be different drivers."
            )

        return cleaned_data

# List of F1 teams for the dropdown
# First item is an empty option shown by default
TEAM_CHOICES = [('', '--- Select a team ---')] + [
    ('Aston Martin', 'Aston Martin'),
    ('Alpine', 'Alpine'),
    ('Audi', 'Audi'),
    ('Cadillac', 'Cadillac'),
    ('Ferrari', 'Ferrari'),
    ('Haas', 'Haas'),
    ('McLaren', 'McLaren'),
    ('Mercedes', 'Mercedes'),
    ('Racing Bulls', 'Racing Bulls'),
    ('Red Bull', 'Red Bull'),
    ('Williams', 'Williams'),
]


class UserProfileForm(forms.ModelForm):
    # ModelForm automatically creates form fields from the UserProfile model
    class Meta:
        model = UserProfile
        fields = ['display_name', 'favourite_team', 'favourite_driver']
        labels = {
            'display_name': 'Display Name',
            'favourite_team': 'Favourite Team',
            'favourite_driver': 'Favourite Driver',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override favourite_team to use a dropdown with predefined choices
        # instead of a free-text input
        self.fields['favourite_team'].widget = forms.Select(
            choices=TEAM_CHOICES, attrs={'class': 'form-select'}
        )
        # Set the driver dropdown to show all drivers
        self.fields['favourite_driver'].queryset = Driver.objects.all()
        # Add Bootstrap styling to all fields
        self.fields['favourite_driver'].widget.attrs['class'] = 'form-select'
        self.fields['display_name'].widget.attrs['class'] = 'form-control'