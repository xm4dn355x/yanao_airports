from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Flights

# Create your views here.
def index(request):
    flights = Flights.objects.all()
    template = loader.get_template('dashboard/index.html')
    context = {
        'flights': flights
    }
    return HttpResponse(template.render(context, request))