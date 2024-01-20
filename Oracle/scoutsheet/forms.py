from django import forms
from .models import ScoutSheet

class ScoutSheetForm(forms.ModelForm):
    DRIVE_TRAIN_CHOICES = [
        ('Unknown', 'Unknown'),
        ('Tank', 'Tank'),
        ('Swerve', 'Swerve'),
        ('Mecanum', 'Mecanum'),
        ('H-Drive', 'H-Drive'),
        ('Omni', 'Omni'),
        ('Other', 'Other'),
    ]
    
    drive_train = forms.ChoiceField(choices=DRIVE_TRAIN_CHOICES)
    
    elevator = forms.BooleanField(required=False)
    shooter = forms.BooleanField(required=False)
    autonomous = forms.BooleanField(required=False)
    
    class Meta:
        model = ScoutSheet
        fields =['elevator', 'shooter', 'autonomous', 'drive_train', 'motor_count']