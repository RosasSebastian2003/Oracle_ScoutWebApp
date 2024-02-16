from django.urls import path
from .views import *

urlpatterns = [
    path('events/all', return_all_events.as_view(), name='get_events'),
    path('events/all/simple', return_all_events_simple.as_view(), name='get_events_simple'),
    path('events/country/<str:country>', return_events_in_country.as_view(), name='get_events_in_country'),
    path('events/state/<str:state>', return_events_in_state.as_view(), name='get_events_in_state'),
    path('events/city/<str:city>', return_events_in_city.as_view(), name='get_events_in_city'),
    path('event/<str:pk>', return_event.as_view(), name='get_event'),
    path('event/simple/<str:pk>', return_event_simple.as_view(), name='get_event_simple'),
]