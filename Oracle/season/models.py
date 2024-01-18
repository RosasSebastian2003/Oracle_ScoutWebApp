from django.db import models

# Create your models here.
    
class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def _verbose_name_plural(self):
        return 'Seasons'

    
class Event(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_prov = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    # Time Bound Data
    start_date = models.DateField()
    end_date = models.DateField()
    
    season = models.ForeignKey(Season, related_name = 'events', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def _verbose_name_plural(self):
        return 'Events'

class Match(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    
    event = models.ForeignKey(Event, related_name = 'matches', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.key
    
    def _verbose_name_plural(self):
        return 'Matches'
    

