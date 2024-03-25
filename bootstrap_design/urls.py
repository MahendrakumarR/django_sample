from django.urls import path
from . import views

urlpatterns = [
    path('', views.boot, name='bootstrap_design')
    
]
