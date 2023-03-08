from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from users.models import Person
from .models import Event, Participation
from .forms import EventForm, EventModelForm


# Create your views here.


def homePage(request):
    return HttpResponse('<h1>Welcome To... </h1>')


def listEventsStatic(request):
    list = [
        {
            'title': 'Event 1',
            'description': 'description 1',
        },
        {
            'title': 'Event 2',
            'description': 'description 2',
        },
        {
            'title': 'Event 3',
            'description': 'description 3',
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list,
        }
    )


@login_required(login_url='/account/login')
def listEvents(request):
    # list = Event.objects.all()
    list = Event.objects.filter(state=True)
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list,
        }
    )


def detailsEvent(request, id):
    event = Event.objects.get(id=id)
    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
        }
    )


def addEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return redirect("events_list")
    return render(request, 'events/events_add.html', {'form': form})


def addEventModel(request):
    form = EventModelForm()
    if request.method == "POST":
        form = EventModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("events_list")
    return render(request, 'events/events_add.html', {'form': form})


# class 
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventModelForm
    success_url = reverse_lazy('events_list')
    login_url = 'login'


class EventsList(ListView):
    model = Event
    template_name = 'events/listEvents.html'
    context_object_name = 'events'
    queryset = Event.objects.filter(state=True)


def participateEvent(request, id):
    event = Event.objects.get(id=id)
    person = Person.objects.get(cin='12345678')
    if Participation.objects.filter(event=event, person=person).count() == 0:
        Participation.objects.create(event=event, person=person)
        event.nbrParticipants += 1
        event.save()
    # autre methode:
    # nb = event.nbrParticipants + 1
    # Event.objects.filter(id=id).update(nbrParticipants=nb)
    return redirect("events_list")


def updateEvent(request, id):
    event = Event.objects.get(id=id)
    form = EventModelForm(instance=event)
    if request.method == "POST":
        form = EventModelForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("events_list")
    return render(request, 'events/events_add.html', {'form': form})


# class based update
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventModelForm
    template_name = 'events/events_add.html'
    success_url = reverse_lazy('events_list')


class deleteEvent(DeleteView):
    model = Event
    success_url = reverse_lazy('events_list')


def deleteEventFn(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect("events_list")


def cancelEvent(request, id):
    event = Event.objects.get(id=id)
    person = Person.objects.get(cin='12345678')
    participation = Participation.objects.filter(event=event, person=person)
    if participation.count() != 0:
        participation.delete()
        event.nbrParticipants -= 1
        event.save()
        messages.add_message(request, messages.SUCCESS, 'Participation annulée')
    return redirect("events_list")


class EventsDetails(DetailView):
    model = Event
