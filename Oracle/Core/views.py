import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from team.models import Team
from season.models import Event, Season

import logging
# Create your views here.
logger = logging.getLogger('admin')

def filter_objects(request):
    option = request.GET.get('option')
    
    logger.info(f'Option: {option}')
    
    events_in_country = Event.objects.filter(country=option)
    events_in_state = Event.objects.filter(state_prov=option)
    events_in_city = Event.objects.filter(city=option)
    
    if events_in_country.exists():
        events = events_in_country # QuerySet
        events_json = serializers.serialize('json', events) # str
        event_dict = json.loads(events_json) # list of dicts
        
        teams = Team.objects.filter(events__in=events) # QuerySet
        teams_json = serializers.serialize('json', teams) # str
        team_dict = json.loads(teams_json) # list of dicts
        
        logger.info(f'Events in country: {event_dict}')
        
        response = JsonResponse({'events':event_dict, 'teams':team_dict})
        logger.info(f'Response: {response}')
        
        return response
    elif events_in_state.exists():
        logger.info(f'Events in state: {events_in_state}')
        events = events_in_state
        events_json = serializers.serialize('json', events)
        
        teams = Team.objects.filter(events__in=events)
        teams_json = serializers.serialize('json', teams)
        
        return JsonResponse({'events':events_json, 'teams':teams_json})
    elif events_in_city.exists():
        logger.info(f'Events in city: {events_in_city}')
        events = events_in_city
        events_json = serializers.serialize('json', events)
        
        teams = Team.objects.filter(events__in=events)
        teams_json = serializers.serialize('json', teams)
        
        return JsonResponse({'events':events_json, 'teams':teams_json})
    else:
        return JsonResponse({'events':None, 'teams':None})
    


def index(request):
    teams = Team.objects.all() 
    
    cities = Event.objects.values('city').distinct()
    countries = Event.objects.values('country').distinct()
    states = Event.objects.values('state_prov').distinct()
    event_names = Event.objects.values('name').distinct()
    
    return render(request, 'Core/index.html', {
                    'teams': teams,
                    'cities': cities,
                    'countries': countries,
                    'states': states,
                    'event_names': event_names,
                  }
                 )
