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

def menuitems(request, dish):
    items = {
        'pasta' : 'Pasta is a types of nuddles',
        'meggie' : 'Maggie is a maggie',
        'samosa' : 'Samosa is a also known as singhda'
    }
    
    description = items[dish]
    
    return HttpResponse(f"<h2> {dish} <h2>" + description)