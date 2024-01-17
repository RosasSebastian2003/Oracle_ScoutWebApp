from typing import Any
import requests
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser
from season.models import Season, Event

class Command(BaseCommand):
    help = 'Fetches events from The Blue Alliance API and saves them to the database'
    
    url = "https://www.thebluealliance.com/api/v3"
    header = {"X-TBA-Auth-Key":"E5xeD6sWIPJe5QDAgtoXzoHkQpKxaoOJlyGXThQBH4SztWmnfEgSbjYLFbC40r1E"}
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('season', type=int, help='The season to fetch events for')
        
    @staticmethod
    def save_events(events: list, season: Season) -> None:
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
                    'season': season
                }
            )
            
            return Command.save_events(events[1:], season)
    
    def get_events(self, season):
        response = requests.get(Command.url + f"/events/{season}/simple", headers = Command.header).json()
        
        Command.save_events(response, Season.objects.get(year=season))
    
    def handle(self, *args, **options):
        return self.get_events(options['season'])
    