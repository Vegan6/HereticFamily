#admin.py
from django.contrib import admin
from HereticFamily.AppData.models import FactWeathercurrent
from HereticFamily.AppData.models import FactTasklist

class WeatherAdmin(admin.ModelAdmin):
  list_display = ('stationid', 'updatedatetime')
  list_display_links = ('stationid', 'updatedatetime')
  #search_fields = ('title', 'content')
  list_per_page = 25
    
class TaskAdmin(admin.ModelAdmin):
  list_display = ('taskid', 'taskname', 'createdby', 'assignedto', 'completed')
  list_display_links = ('taskid', 'taskname')
  #search_fields = ('title', 'content')
  list_per_page = 25
    
admin.site.register(FactWeathercurrent, WeatherAdmin)
admin.site.register(FactTasklist, TaskAdmin)