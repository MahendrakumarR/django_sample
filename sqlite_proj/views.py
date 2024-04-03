from django.shortcuts import render


def data (request):
    return render(request, "sql_front.html")

# Create your views here.
