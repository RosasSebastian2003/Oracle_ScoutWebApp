from typing import Any
import requests
from django.core.management.base import BaseCommand
from team.models import Team

class Command(BaseCommand):
    help = 'Fetches all teams participating in the year 2024 from The Blue Alliance and stores them in the database'
    
    url = "https://www.thebluealliance.com/api/v3"
    header = {"X-TBA-Auth-Key":"E5xeD6sWIPJe5QDAgtoXzoHkQpKxaoOJlyGXThQBH4SztWmnfEgSbjYLFbC40r1E"}
    
    @staticmethod
    def store_teams(teams: list) -> None:
        if len(teams) == 0:
            return
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
            return Command.store_teams(teams[1:])
        
    @staticmethod
    def get_teams_by_year(page = 0) -> None:
        response = requests.get(Command.url + "/teams/2023/" + str(page) + "/simple", headers=Command.header).json()
        
        if len(response) == 0:
            return
        else:
            Command.store_teams(response)
            return Command.get_teams_by_year(page + 1)
        
    def handle(self, *args, **options):
        return self.get_teams_by_year()
    
    
        