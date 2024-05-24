from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('homepage/', views.homepage),
    path('display_date/', views.display_date),
    path('dishes/<str:dish>', views.menuitems), #dish=pasta
    
]