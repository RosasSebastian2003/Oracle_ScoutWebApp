from typing import Any
import requests
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser

from team.models import Team
from season.models import Season, Event, Match

from django.core.exceptions import ObjectDoesNotExist
import logging

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
        if len(matches) == 0:
            return
        elif Command.exists(Match, key=matches[0]["key"]):
            return Command.save_matches(matches[1:], event)
        else:
            match, created =Match.objects.update_or_create(
                key = matches[0]["key"],
                defaults={
                    'event': event,
                }
            )
            
            blue_alliance = Team.objects.filter(key__in=matches[0]["alliances"]["blue"]["team_keys"])
            red_alliance = Team.objects.filter(key__in=matches[0]["alliances"]["red"]["team_keys"])
            
            match.blue_alliance.set(blue_alliance)
            match.red_alliance.set(red_alliance)
            
            return Command.save_matches(matches[1:], event)
    
    # Save teams to the database
    @staticmethod
    def save_teams_in_event(teams: list) -> None:
        if len(teams) == 0:
            return 
        elif Command.exists(Team, number=teams[0]["team_number"]):
            return Command.save_teams_in_event(teams[1:])
        else:
            Team.objects.update_or_create(
                number=teams[0]["team_number"],
                defaults={
                    'key': teams[0]['key'],
                    'name': teams[0]['name'],
                    'nickname': teams[0]['nickname'],
                    'city': teams[0]['city'],
                    'state_prov': teams[0]['state_prov'],
                    'country': teams[0]['country']    
                }
            )
            
            return Command.save_teams_in_event(teams[1:])
        
        
        
    
    # Save events to the database
    @staticmethod
    def save_events(events: list, season: Season) -> None:
        if len(events) == 0:
            return
        elif Command.exists(Event, key=events[0]["key"]):
            return Command.save_events(events[1:], season)
        else:
            event, created = Event.objects.update_or_create(
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
            
            try:
                teams = requests.get(Command.url + f"/event/{events[0]['key']}/teams/simple", headers = Command.header).json()
                Command.save_teams_in_event(teams)
            except requests.JSONDecodeError:
                teams = requests.get(Command.url + f"/event/{events[0]['key']}/teams/simple", headers = Command.header).json()
                logger.info(teams.status_code)
                logger.info(teams.text)
            
            try:
                matches = requests.get(Command.url + f"/event/{events[0]['key']}/matches/simple", headers = Command.header).json()
                Command.save_matches(matches, event)
            except requests.JSONDecodeError:
                matches = requests.get(Command.url + f"/event/{events[0]['key']}/matches/simple", headers = Command.header).json()
                logger.info(matches.status_code)
                logger.info(matches.text)
            
            return Command.save_events(events[1:], season)
    
    def get_events(self, season):
        response = requests.get(Command.url + f"/events/{season}/simple", headers = Command.header).json()
        
        Command.save_events(response, Season.objects.get(year=season))
    
    def handle(self, *args, **options):
        return self.get_events(options['season'])
    