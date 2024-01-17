from typing import Any
import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from season.models import Season, Event

class Command(BaseCommand):
    help = 'Deletes all data fetched from The Blue Alliance'
    
    testSeason = Season.objects.get(year=2023)
    
    url = "https://www.thebluealliance.com/api/v3"
    header = {"X-TBA-Auth-Key":"E5xeD6sWIPJe5QDAgtoXzoHkQpKxaoOJlyGXThQBH4SztWmnfEgSbjYLFbC40r1E"}
    
    @staticmethod
    def save_events(events: list) -> None:
        if len(events) == 0:
            return
        else:
            Event.objects.update_or_create(
                key = events[0]["key"],
                defaults={
                    'name': events[0]['name'],
                    'city': events[0]['city'],
                    'state_prov': events[0]['state_prov'],
                    'country': events[0]['country'],
                    'start_date': datetime.strptime(events[0]['start_date'], '%Y-%m-%d').date(),
                    'end_date': datetime.strptime(events[0]['end_date'], '%Y-%m-%d').date(),
                    'season': Command.testSeason
                }
            )
            
            return Command.save_events(events[1:])
    
    def get_events(self):
        response = requests.get(Command.url + "/events/2023/simple", headers = Command.header).json()
        
        Command.save_events(response)
    
    def handle(self, *args, **options):
        return self.get_events()
    