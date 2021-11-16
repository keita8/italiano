from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ['title', 'date']
	ordering = ['-date']
	search_fields = ['title']


admin.site.register(Event, EventAdmin)
