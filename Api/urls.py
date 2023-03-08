from django.urls import path
from .views import *

urlpatterns = [
    path('', getEvents),
    path('add/', addEvent),
    path('update/<int:id>', updateEvent),
    path('delete/<int:id>', deleteEvent),
]
