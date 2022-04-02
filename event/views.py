from django.shortcuts import render
from .models import Event

""" eventList = [
    {
        'name': 'event1'
    },
    {
        'name': 'event2'
    }
]
 """


def events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'ecell_events/events.html', context)
