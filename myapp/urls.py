from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('homepage/', views.homepage),
    path('display_dat/', views.display_date),
    path('form/', views.form_view),
]