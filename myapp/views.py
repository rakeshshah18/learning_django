from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("Welcome to the Django homepage!")

def menu(request):
    mainmenu = {'mains': [
        {'name': "rakesh", 'age': "25"},
        {'name': "suresh", 'age': "30"},
        {'name': "mahesh", 'age': "35"},
    ]}
    return render(request, "menu.html", mainmenu)