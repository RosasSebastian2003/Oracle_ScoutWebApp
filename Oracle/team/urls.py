from django.urls import path
from .views import return_all_teams, return_team

urlpatterns = [
    path('team/all', return_all_teams.as_view(), name='get_teams'),
    path('team/<int:pk>', return_team.as_view(), name='get_team'),
]