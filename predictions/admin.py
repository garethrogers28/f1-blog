
"""
Admin configuration for the predictions app models.
Registers Driver, Race, Prediction, RaceResult, and UserProfile with custom admin classes.
"""
from django.contrib import admin
from .models import Driver, Race, Prediction, RaceResult, UserProfile


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'number')
    list_filter = ('team',)
    search_fields = ('name',)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'circuit', 'date', 'prediction_deadline', 'is_completed')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_completed',)


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'race', 'pole_driver', 'p1_driver', 'p2_driver', 'p3_driver')
    list_filter = ('race',)


@admin.register(RaceResult)
class RaceResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'pole_driver', 'p1_driver', 'p2_driver', 'p3_driver')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'favourite_team', 'favourite_driver')
