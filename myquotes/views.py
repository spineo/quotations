from django.views.generic.list import ListView

from myquotes.models import Event

# 'context_object_name' by default is 'event_list' but can be overriden
#
class EventListView(ListView):
    model = Event
    template_name = "event.html"
