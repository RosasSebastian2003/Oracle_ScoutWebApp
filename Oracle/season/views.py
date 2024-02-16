import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from rest_framework import generics
from .serializers import EventSerializer, EventSimpleSerializer
from .models import Event

# Create your views here.
# API endpoints
class return_all_events(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class return_all_events_simple(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSimpleSerializer

class return_event(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class return_event_simple(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Find by location
class return_events_in_country(generics.ListAPIView):
    serializer_class = EventSimpleSerializer
    lookup_field = 'country'
    
    def get_queryset(self):
        country = self.kwargs['country']
        return Event.objects.filter(country=country)
    
class return_events_in_state(generics.ListAPIView):
    serializer_class = EventSimpleSerializer
    lookup_field = 'state_prov'
    
    def get_queryset(self):
        state_prov = self.kwargs['state_prov']
        return Event.objects.filter(state_prov=state_prov)

class return_events_in_city(generics.ListAPIView):
    serializer_class = EventSimpleSerializer
    lookup_field = 'city'
    
    def get_queryset(self):
        city = self.kwargs['city']
        return Event.objects.filter(city=city)