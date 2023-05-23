from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),
    path('add/', addEvent, name="events_add"),
    path('details/<int:id>', detailsEvent, name="events_details"),
    path('Participate/<int:id>', participateEvent, name="events_Participate"),
    path('update/<int:id>', updateEvent, name="events_update"),
    path('updateView/<int:pk>', EventUpdateView.as_view(), name="events_updateView"),
    path('deleteView/<int:pk>', deleteEvent.as_view(), name="events_delete"),
    path('delete/<int:id>', deleteEventFn, name="events_delete"),
    path('CancelEvent/<int:id>', cancelEvent, name="events_cancel"),
    path('listEvents/', EventsList.as_view(), name="events_listC"),
    path('eventsDetails/<int:pk>', EventsDetails.as_view(), name="events_DetailsC"),
]
