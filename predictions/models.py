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
    
class RaceResult(models.Model):
    race = models.OneToOneField(Race, on_delete=models.CASCADE, related_name='result')
    pole_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='pole_results')
    p1_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p1_results')
    p2_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p2_results')
    p3_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='p3_results')

    def __str__(self):
        return f"Result: {self.race.name}"
