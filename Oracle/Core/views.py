from django.shortcuts import render

from team.models import Team
from season.models import Event, Season
# Create your views here.
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
