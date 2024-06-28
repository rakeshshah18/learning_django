from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.forms import LogForm

from .models import Logger

import logging


logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    return HttpResponse('Hello, Django!')

def homepage(request):
    return HttpResponse("Welcome to the Django homepage!")

def display_date(request):
    return HttpResponse("This page was served at " + str(datetime.today().year))

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            data = Logger.objects.create(first_name=first_name, last_name=last_name)
            
            return HttpResponse("Thank you for submitting the form!")
            
    context = {'form': form}
    return render(request, 'form.html', context)