from django.db import models

from team.models import Team

# Create your models here.
    
class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

    
class Event(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_prov = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    
    # Time Bound Data
    start_date = models.DateField()
    end_date = models.DateField()
    
    season = models.ForeignKey(Season, related_name = 'events', on_delete = models.CASCADE)
    
    class Meta:
        index_together = [
            ['city', 'state_prov', 'country'],
            ['state_prov', 'country'],
            ['city', 'country'],
        ]
        
    def __str__(self):
        return self.name
    

class Match(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    
    event = models.ForeignKey(Event, related_name = 'matches', on_delete = models.CASCADE)
    
    blue_alliance = models.ManyToManyField(Team, related_name = 'blue_alliance')
    red_alliance = models.ManyToManyField(Team, related_name = 'red_alliance')
    
    class Meta:
        verbose_name_plural = 'Matches'
        index_together = [
            ['event', 'key'],
        ]
    
    def __str__(self):
        return self.key
    

