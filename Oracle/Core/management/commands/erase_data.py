from typing import Any

from django.core.management.base import BaseCommand

# In app imports    
from team.models import Team
from season.models import Season, Event

class Command(BaseCommand):
    help = 'Deletes all data fetched from The Blue Alliance'
        
    def delete(self):
        Team.objects.all().delete()
        Season.objects.all().delete()
    
    def handle(self, *args, **options):
        return self.delete()
    
