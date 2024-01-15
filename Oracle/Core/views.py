from django.shortcuts import render
from team.models import Team
# Create your views here.
def index(request):
    teams = Team.objects.all() [:10]
    
    return render(request, 'Core/index.html', {
        'teams': teams,
        })
