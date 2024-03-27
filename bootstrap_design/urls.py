from django.urls import path
from . import views

urlpatterns = [
    path('', views.boot, name='boot'),
    path('boot_out', views.boot_out, name='boot_out')
    
]
   