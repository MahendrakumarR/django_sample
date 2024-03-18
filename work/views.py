from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("your name is : ")         # this print only the hello world

def  brain(request):                           # same as the above code
    return HttpResponse("Hello ,Brain ")

def own(request, name):
    return render(request, "work/own.html", {'name':name})   # using html for user input value

# Create your views here.
