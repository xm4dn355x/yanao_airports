from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the dashboard index.")


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