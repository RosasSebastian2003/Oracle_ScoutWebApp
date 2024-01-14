from django.db import models

# Create your models here.
class Team(models.Model):
    number = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    
    city = models.CharField(max_length=100)
    state_prov = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def _verbose_name_plural(self):
        return 'Teams'