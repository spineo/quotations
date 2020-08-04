from django.http import HttpResponse

from django.template import loader

from myquotes.models import Quotation, Event

import random
import datetime

# Return a random quotation associated with an author event for today
# or just a random quotation if now event found
#
def index(request):
    now = datetime.datetime.now()

    year      = now.year
    month     = now.month
    day       = now.day

    # Query Event
    #
    events_count   = Event.objects.filter(month=month).count()
    event_rand_num = random.randint(1, events_count)
    
    event          = Event.objects.filter(month=month)[event_rand_num:event_rand_num+1]
    if event:
        print(event[0])

    all_count = Quotation.objects.count()
    rand_num  = random.randint(1, all_count)

    quotation = Quotation.objects.all()[rand_num:rand_num+1]

    template = loader.get_template('index.html')
    context = {
        'quotation': quotation,
    }
    return HttpResponse(template.render(context, request))
