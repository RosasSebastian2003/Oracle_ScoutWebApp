from django.contrib import admin
from .models import Team
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('number', 'nickname', 'city', 'state_prov', 'country')
    list_filter = ('city', 'state_prov', 'country')
    
    search_fields = ['number', 'nickname', 'city', 'state_prov', 'country']
    
admin.site.register(Team, TeamAdmin)