from rest_framework import serializers
from .models import Season, Event

# Season
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
 
# Event       
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class EventSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['key', 'name', 'city', 'state_prov', 'country', 'teams']