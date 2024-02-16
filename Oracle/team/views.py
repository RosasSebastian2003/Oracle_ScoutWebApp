import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

from rest_framework import generics
from .serializers import TeamSerializer
from .models import Team

# Create your views here.
# API endpoints

# Variable names matter, abstract classes?
class return_all_teams(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class =  TeamSerializer

class return_team(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
