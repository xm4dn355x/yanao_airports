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


def show_sly(request):
    flights = Flights.objects.all()
    delayed = Flights.objects.all()
    template = loader.get_template('dashboard/index.html')
    context = {
        'flights': flights,
        'delayed': delayed,
    }
    return HttpResponse(template.render(context, request))


def show_noj(request):
    flights = Flights.objects.all()
    delayed = Flights.objects.all()
    template = loader.get_template('dashboard/index.html')
    context = {
        'flights': flights,
        'delayed': delayed,
    }
    return HttpResponse(template.render(context, request))


def show_nux(request):
    flights = Flights.objects.all()
    delayed = Flights.objects.all()
    template = loader.get_template('dashboard/index.html')
    context = {
        'flights': flights,
        'delayed': delayed,
    }
    return HttpResponse(template.render(context, request))


def show_nym(request):
    flights = Flights.objects.all()
    delayed = Flights.objects.all()
    template = loader.get_template('dashboard/index.html')
    context = {
        'flights': flights,
        'delayed': delayed,
    }
    return HttpResponse(template.render(context, request))


def show_sbt(request):
    flights = Flights.objects.all()
    delayed = Flights.objects.all()
    template = loader.get_template('dashboard/index.html')
    context = {
        'flights': flights,
        'delayed': delayed,
    }
    return HttpResponse(template.render(context, request))