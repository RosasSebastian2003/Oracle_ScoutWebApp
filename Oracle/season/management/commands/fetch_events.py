from typing import Any
import requests
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser

from team.models import Team
from season.models import Season, Event, Match

from django.core.exceptions import ObjectDoesNotExist
import logging
import json

logger = logging.getLogger('admin')

class Command(BaseCommand):
    help = 'Fetches events from The Blue Alliance API and saves them to the database'
    
    url = "https://www.thebluealliance.com/api/v3"
    header = {"X-TBA-Auth-Key":"E5xeD6sWIPJe5QDAgtoXzoHkQpKxaoOJlyGXThQBH4SztWmnfEgSbjYLFbC40r1E"}
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('season', type=int, help='The season to fetch events for')
    
    # Check if a given object already exists in the database
    @staticmethod
    def exists(model, **kwargs) -> bool:
        try:
            model.objects.get(**kwargs)
            return True
        except ObjectDoesNotExist:
            return False
        
    # Save matches to the database and group teams into alliances
    @staticmethod
    def save_matches(matches: list, event: Event) -> None:
        for match_data in matches:
            if not Command.exists(Match, key=match_data["key"]):
                match, created = Match.objects.update_or_create(
                    key = match_data["key"],
                    defaults={
                        'event': event,
                    }
                )
           
                blue_alliance = Team.objects.filter(key__in=match_data["alliances"]["blue"]["team_keys"])
                # logger.info(blue_alliance)
                match.blue_alliance.set(blue_alliance)
                
                red_alliance = Team.objects.filter(key__in=match_data["alliances"]["red"]["team_keys"])
                # logger.info(red_alliance)
                match.red_alliance.set(red_alliance)
    
    
    # Save events to the database
    @staticmethod
    def save_events(events: list, season: Season) -> None:
        for event in events:
            
            defaults = {
                    'name': event['name'],
                    'week': (event['week'] + 1) if event['week'] != None else Event._meta.get_field('week').get_default(),
                    'city': event['city'],
                    'state_prov': event['state_prov'],
                    'country': event['country'],
                    'start_date': datetime.strptime(event['start_date'], '%Y-%m-%d').date(),
                    'end_date': datetime.strptime(event['end_date'], '%Y-%m-%d').date(),
                    'season': season
                }
            
            newEvent, created = Event.objects.update_or_create(
                key = event["key"],
                defaults=defaults
            )
                
            matches = requests.get(Command.url + f"/event/{event['key']}/matches/simple", headers = Command.header).json()
            
            # teams in event
            try: 
                team_list = requests.get(Command.url + f"/event/{event['key']}/teams/keys", headers = Command.header).json()
                teams = Team.objects.filter(key__in=team_list)
                newEvent.teams.set(teams)
            except json.decoder.JSONDecodeError:
                logger.info(f"Error: {event['key']}")
            
            Command.save_matches(matches, newEvent)
                
    def get_events(self, season):
        response = requests.get(Command.url + f"/events/{season}", headers = Command.header).json()
        
        Command.save_events(response, Season.objects.get(year=season))
    
    def handle(self, *args, **options):
        return self.get_events(options['season'])
    