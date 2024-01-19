from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME

import logging

# In app imports
from .models import Season, Event, Match
from .forms import UpdateCountryForm

# Register your models here.
logger = logging.getLogger('admin')

admin.site.register(Season)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country',)
    list_filter = ('season', 'country', 'week',)
    ordering = ('start_date', 'week',)
    
    # Register custom admin views as if we did it in urls.py
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'correct_country_name',
                self.admin_site.admin_view(self.update_country_view),
                name='correct_country_name',
            ),
        ]
        return custom_urls + urls
    
    def update_country(self, request, queryset):
        form = None
        
        self.message_user(request, f'{queryset.count()} events selected')
        
        if 'apply' in request.POST:
            form = UpdateCountryForm(request.POST)
            
            logger.info(f'Form data: {request.POST}')
            
            if form.is_valid():
                country_name = form.cleaned_data['country_name']
                
                queryset.update(country=country_name)
                    
                self.message_user(request, f'Updated countries to {country_name}')
                
                url = reverse('admin:season_event_changelist')
                return HttpResponseRedirect(url)
            
        if not form:
            form = UpdateCountryForm(initial={'_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)})
            
        
        
        return render(request, 'admin/update_country.html', 
                      {
                        'items': queryset, 
                        'form': form
                      }
                     )

    update_country.short_description = 'Update Country'
    actions = [update_country]
    
    def update_country_view(self, request):
        selected_items = request.POST.getlist(ACTION_CHECKBOX_NAME)
        
        queryset = Event.objects.filter(pk__in=selected_items)
       
        return self.update_country(request, queryset)
    
admin.site.register(Event, EventAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('key', 'event',)
    filter_horizontal = ('blue_alliance', 'red_alliance',)
    search_fields = ('key', 'event__city')
    
admin.site.register(Match, MatchAdmin)