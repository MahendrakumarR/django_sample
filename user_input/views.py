from django.shortcuts import render
from django.http import HttpResponse


def user_input(request):
    return render(request, 'user_input.html')


    

# Create your views here.
