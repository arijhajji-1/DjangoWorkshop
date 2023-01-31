from django.contrib import admin
from .models import *
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    ordering = ('username',)
    list_filter = ('username',)
# Register your models here.
admin.site.register(Person, PersonAdmin)
