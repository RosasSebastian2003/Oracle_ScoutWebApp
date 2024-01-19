from typing import Any

from django.core.management.base import BaseCommand

# In app imports    
from team.models import Team
from season.models import Season, Event, Match

class Command(BaseCommand):
    help = 'Deletes all data fetched from The Blue Alliance'
        
    def delete(self):
        Team.objects.all().delete()
        Match.objects.all().delete()
        Event.objects.all().delete()
    
    def handle(self, *args, **options):
        return self.delete()
    
