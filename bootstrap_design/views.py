from django.shortcuts import render


def boot(request):
    return render(request, "boot.html")
# Create your views here.
