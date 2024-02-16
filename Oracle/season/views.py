import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import Event

# Create your views here.
# API endpoints
def return_all_events(request):
    events = Event.objects.all()
    events_json = serializers.serialize('json', events)
    events_dict = json.loads(events_json)
    
    return JsonResponse({'events':events_dict})

def return_events_in_country(request, country):    
    events = Event.objects.filter(country=country)
    events_json = serializers.serialize('json', events)
    events_dict = json.loads(events_json)
    
    return JsonResponse({'events':events_dict})

def return_events_teams_in_state(request, state):
    events = Event.objects.filter(state_prov=state)
    events_json = serializers.serialize('json', events)
    events_dict = json.loads(events_json)
    
    return JsonResponse({'events':events_dict})
    
def return_events_teams_in_city(request, city):
    events = Event.objects.filter(city=city)
    events_json = serializers.serialize('json', events)
    events_dict = json.loads(events_json)
    
    return JsonResponse({'events':events_dict})

