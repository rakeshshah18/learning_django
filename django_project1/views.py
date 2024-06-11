from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("404: Yeh kya search kar diya re!")

def home(request):
    return HttpResponse('Hello, Django!')