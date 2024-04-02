from django.urls import path
from . import views

urlpatterns = [
    path('', views.sqlite_proj, name='sqlite_proj'),
]