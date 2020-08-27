from django.http import HttpResponse

from django.template import loader

from myquotes.models import Quotation, Event, EventAuthor

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

    # Initialize
    #
    event          = ''
    author         = ''
    quotation      = ''

    # Query Events
    #
    events_count   = Event.objects.filter(month=month).count()
    event_rand_num = random.randint(1, events_count)

    event_author   = EventAuthor.objects.select_related().filter(event__month=month)[event_rand_num-1:event_rand_num]
    if event_author:
        event     = event_author[0].event
        author    = event_author[0].author

    if event and author:
        # Get a random quotation associated with that author
        #
        quotes_count    = Quotation.objects.filter(author=author).count()
        quotes_rand_num = random.randint(1, quotes_count)
        quotation       = Quotation.objects.filter(author=author)[quotes_rand_num-1:quotes_rand_num]

    # Print the random quotation
    #
    else:
        all_count = Quotation.objects.count()
        rand_num  = random.randint(1, all_count)

        quotation = Quotation.objects.all()[rand_num-1:rand_num]

    # Display the random quotation
    #
    template = loader.get_template('index.html')
    context = {
        'event': event,
        'quotation': quotation,
    }

    return HttpResponse(template.render(context, request))
