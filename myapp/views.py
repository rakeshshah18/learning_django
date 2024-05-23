from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse('Hello, Django!')

def homepage(request):
    return HttpResponse("Welcome to the Django homepage!")

def display_date(request):
    return HttpResponse("This page was served at " + str(datetime.today().year))