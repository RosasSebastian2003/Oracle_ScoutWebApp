from django.urls import path
from . import views

urlpatterns = [
    path('api/events', views.return_all_events, name='get_events'),
    path('api/events/country/<str:country>', views.return_events_in_country, name='get_events_in_country'),
    path('api/events/state/<str:state>', views.return_events_teams_in_state, name='get_events_in_state'),
    path('api/events/city/<str:city>', views.return_events_teams_in_city, name='get_events_in_city'),
]