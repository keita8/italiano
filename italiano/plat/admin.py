from django.contrib import admin
from .models import Plat
# Register your models here.

class PlatAdmin(admin.ModelAdmin):
	list_display = ['title', 'price']
	search_fields = [ 'title','price']


admin.site.register(Plat, PlatAdmin)