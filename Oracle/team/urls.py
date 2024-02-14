from django.urls import path
from . import views

urlpatterns = [
    path('api/teams', views.return_all_teams, name='get_teams'),
    path('api/teams/<int:team_number>', views.return_team, name='get_team'),
]