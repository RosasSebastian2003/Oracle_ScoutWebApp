import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

from models import Team

# Create your views here.
# API endpoints
def return_all_teams(request):
    teams = Team.objects.all()
    teams_json = serializers.serialize('json', teams)
    teams_dict = json.loads(teams_json)
    
    return JsonResponse({'teams':teams_dict})

def return_team(request, team_number):
    team = Team.objects.get(number=team_number)
    team_json = serializers.serialize('json', team)
    team_dict = json.loads(team_json)
    
    return JsonResponse({'team':team_dict})