from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'state')
    ordering = ('title',)
    list_filter = ('state',)
    search_fields = ['title', 'category']
    list_per_page = 5
    #fields = ('organizers',
             # 'state',
              #('title','description'),
             # 'eventImage',
              #  ('category', 'nbrParticipants'),
              #  'eventDate',
              #  ('created_at', 'updated_at')
             # )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (
            'STATE', {
                'classes' : ('collapse',),
                'fields': ('state','created_at', 'updated_at')
            }

        ),
        (
            'ABOUT', {
                'fields': ('title', 'description', 'eventImage', 'category', 'nbrParticipants',
                           'eventDate')
            }
        )


        )

# Register your models here.
admin.site.register(Event, EventAdmin)
