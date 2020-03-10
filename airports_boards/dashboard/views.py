"""
Airports dashboard views.py
"""


from django.db.models import Q
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Flights

# Create your views here.
def index(request):
    problem_flights = Flights.objects.filter(Q(status='ОТМЕНЕН') | Q(status='ЗАДЕРЖАН') | Q(status='НЕИЗВЕСТЕН'))\
        .order_by('orig_airport', 'flight_type')
    template = loader.get_template('dashboard/index.html')
    context = {
        'problems': problem_flights,
    }
    return HttpResponse(template.render(context, request))


def show_sly(request):
    airport = 'Салехард'
    flights = Flights.objects.filter(orig_airport=airport)
    problem_flights = Flights.objects.filter(orig_airport=airport)\
        .filter(Q(status='ОТМЕНЕН') | Q(status='ЗАДЕРЖАН')).order_by('orig_airport', 'flight_type')
    arrivals = flights.filter(flight_type='ПРИЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    departures = flights.filter(flight_type='ВЫЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    template = loader.get_template('dashboard/index.html')
    context = {
        'problems': problem_flights,
        'arrivals': arrivals,
        'departures': departures
    }
    return HttpResponse(template.render(context, request))


def show_noj(request):
    airport = 'Ноябрьск'
    flights = Flights.objects.filter(orig_airport=airport)
    problem_flights = Flights.objects.filter(orig_airport=airport) \
        .filter(Q(status='ОТМЕНЕН') | Q(status='ЗАДЕРЖАН')).order_by('orig_airport', 'flight_type')
    arrivals = flights.filter(flight_type='ПРИЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    departures = flights.filter(flight_type='ВЫЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    template = loader.get_template('dashboard/index.html')
    context = {
        'problems': problem_flights,
        'arrivals': arrivals,
        'departures': departures
    }
    return HttpResponse(template.render(context, request))


def show_nux(request):
    airport = 'Новый Уренгой'
    flights = Flights.objects.filter(orig_airport=airport)
    problem_flights = Flights.objects.filter(orig_airport=airport) \
        .filter(Q(status='ОТМЕНЕН') | Q(status='ЗАДЕРЖАН')).order_by('orig_airport', 'flight_type')
    arrivals = flights.filter(flight_type='ПРИЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    departures = flights.filter(flight_type='ВЫЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    template = loader.get_template('dashboard/index.html')
    context = {
        'problems': problem_flights,
        'arrivals': arrivals,
        'departures': departures
    }
    return HttpResponse(template.render(context, request))


def show_nym(request):
    airport = 'Надым'
    flights = Flights.objects.filter(orig_airport=airport)
    problem_flights = Flights.objects.filter(orig_airport=airport) \
        .filter(Q(status='ОТМЕНЕН') | Q(status='ЗАДЕРЖАН')).order_by('orig_airport', 'flight_type')
    arrivals = flights.filter(flight_type='ПРИЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    departures = flights.filter(flight_type='ВЫЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    template = loader.get_template('dashboard/index.html')
    context = {
        'problems': problem_flights,
        'arrivals': arrivals,
        'departures': departures
    }
    return HttpResponse(template.render(context, request))


def show_sbt(request):
    airport = 'Сабетта'
    flights = Flights.objects.filter(orig_airport=airport)
    problem_flights = Flights.objects.filter(orig_airport=airport) \
        .filter(Q(status='ОТМЕНЕН') | Q(status='ЗАДЕРЖАН')).order_by('orig_airport', 'flight_type')
    arrivals = flights.filter(flight_type='ПРИЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    departures = flights.filter(flight_type='ВЫЛЕТ').exclude(status='ОТМЕНЕН').exclude(status='ЗАДЕРЖАН')
    template = loader.get_template('dashboard/index.html')
    context = {
        'problems': problem_flights,
        'arrivals': arrivals,
        'departures': departures
    }
    return HttpResponse(template.render(context, request))