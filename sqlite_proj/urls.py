from django.urls import path
from . import views

urlpatterns = [
    path('', views.data, name='sqlite_proj'),
]