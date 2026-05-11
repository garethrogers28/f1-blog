from django.urls import path
from . import views

urlpatterns = [
    path('races/', views.race_list, name='race_list'),
    path('races/<slug:slug>/', views.race_detail, name='race_detail'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]