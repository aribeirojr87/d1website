from django.contrib import admin
from django.urls import path
import players.views

urlpatterns = [
    path('players', players.views.HighScoresView.as_view(), name='players'),
]
