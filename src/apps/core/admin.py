from django.contrib import admin
from .models import Application
#from django_celery_beat.models import PeriodicTask, IntervalSchedule

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'github', 'repository']
    list_display_links = ['id', 'github', 'repository']
    search_fields = ['id', 'github', 'repository']
    list_per_page = 25
    ordering = ['-id']


#admin.site.register(PeriodicTask)
#admin.site.register(IntervalSchedule)

