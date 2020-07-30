from django.http import HttpResponse

from django.template import loader

from myquotes.models import Quotation

import random

def index(request):

    count       = Quotation.objects.count()
    rand_num    = random.randint(1, count)

    quotation   = Quotation.objects.all()[rand_num:rand_num+1]

    template = loader.get_template('index.html')
    context = {
        'quotation': quotation,
    }
    return HttpResponse(template.render(context, request))
