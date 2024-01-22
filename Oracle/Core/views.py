from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from team.models import Team
from season.models import Event, Season
# Create your views here.
def filter_objects(request):
    option = request.GET.get('option')
    
    events_in_country = Event.objects.filter(country=option)
    events_in_state = Event.objects.filter(state_prov=option)
    events_in_city = Event.objects.filter(city=option)
    
    if events_in_country.exists():
        events = events_in_country
        events_json = serializers.serialize('json', events)
        
        teams = Team.objects.filter(events__in=events)
        teams_json = serializers.serialize('json', teams)
        
        return JsonResponse({'events':events_json, 'teams':teams_json})
    elif events_in_state.exists():
        events = events_in_state
        events_json = serializers.serialize('json', events)
        
        teams = Team.objects.filter(events__in=events)
        teams_json = serializers.serialize('json', teams)
        
        return JsonResponse({'events':events_json, 'teams':teams_json})
    elif events_in_city.exists():
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
