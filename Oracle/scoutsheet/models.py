from django.db import models

# In app Imports
from Oracle.team.models import Team
from Oracle.season.models import Season

# Create your models here.
class ScoutSheet(models.Model):
    team = models.OneToOneField(Team, on_delete = models.CASCADE, primary_key = True)
    season = models.ForeignKey(Season, related_name = "scout_sheets", on_delete = models.CASCADE)
    
    # Boolean fields
    elevator = models.BooleanField(default=False)
    shooter = models.BooleanField(default=False)
    autonomous = models.BooleanField(default=False)
    # Dropdown on hot effective the autonomus period was
    
    zone = models.BooleanField(null=True) # true = Speaker, false = Amp
    robot_type = models.BooleanField(null=True) # true = Ofensive, false = Defensive
    
    drive_train = models.CharField(max_length=100, default="Unknown")
    motor_count = models.IntegerField(default=0)