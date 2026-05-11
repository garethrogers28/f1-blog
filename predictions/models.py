from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    number = models.IntegerField()

    class Meta:
        ordering = ['team', 'name']

    def __str__(self):
        return f"{self.name} ({self.team})"
    
class Race(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    circuit = models.CharField(max_length=200)
    date = models.DateField()
    prediction_deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.name} - {self.date}"
    

class Prediction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='predictions')
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='predictions')
    pole_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='pole_predictions')
    p1_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p1_predictions')
    p2_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p2_predictions')
    p3_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p3_predictions')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'race']

    def __str__(self):
        return f"{self.user.username} - {self.race.name}"
    
    def calculate_score(self):
        try:
            result = self.race.result
        except RaceResult.DoesNotExist:
            return 0
        score = 0
        # Using _id compares the foreign key IDs directly in Python
        # This avoids loading the full Driver object from the database
        # Django automatically creates _id attributes for ForeignKey fields
        if self.pole_driver_id == result.pole_driver_id:
            score += 5
        if self.p1_driver_id == result.p1_driver_id:
            score += 10
        if self.p2_driver_id == result.p2_driver_id:
            score += 5
        if self.p3_driver_id == result.p3_driver_id:
            score += 3
        return score
    
class RaceResult(models.Model):
    race = models.OneToOneField(Race, on_delete=models.CASCADE, related_name='result')
    pole_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='pole_results')
    p1_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p1_results')
    p2_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p2_results')
    p3_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p3_results')

    def __str__(self):
        return f"Result: {self.race.name}"
    
class UserProfile(models.Model):
    # Each user gets exactly one profile (OneToOneField)
    # If the user is deleted, their profile is deleted too (CASCADE)
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, related_name='profile'
    )
    # Optional display name shown instead of username on the dashboard
    display_name = models.CharField(max_length=100, blank=True)
    # User's favourite team stored as text (blank=True means it's optional)
    favourite_team = models.CharField(max_length=200, blank=True)
    # User's favourite driver linked to the Driver model
    # SET_NULL means if a driver is deleted, this field becomes None
    # null=True allows the database column to be empty
    # blank=True allows the form field to be left empty
    favourite_driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='fans'
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
