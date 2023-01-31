from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'state')
    ordering = ('title',)
    list_filter = ('state',)

# Register your models here.
admin.site.register(Event, EventAdmin)
