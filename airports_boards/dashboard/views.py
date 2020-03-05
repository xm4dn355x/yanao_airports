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
    return HttpResponse("This is SLY Landing page")


def show_noj(request):
    return HttpResponse("This is NOJ landing page")


def show_nux(request):
    return HttpResponse("This is NUX landing page")


def show_nym(request):
    return HttpResponse("This is NYM landing page")


def show_sbt(request):
    return HttpResponse("This is SBT landing page")