from typing import Any
import requests
from django.core.management.base import BaseCommand
from team.models import Team

class Command(BaseCommand):
    help = 'Deletes all data fetched from The Blue Alliance'
    
    def delete(self):
        Team.objects.all().delete()
    
    def handle(self, *args, **options):
        return self.delete()
    
    def fetch_teams(self) -> None:
        Command.delete()
        