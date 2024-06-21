from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('display_date/', views.display_date, name='display_date'),
    path('display_forms/', views.display_forms, name='display_forms'),
]
