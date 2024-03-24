from django.shortcuts import render
from django.http import HttpResponse


def user_input(request):
    return render(request, 'user.html')
def user_output(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    return render(request, 'user_output.html', {'name':name, 'email':email, 'phone':phone})

    

# Create your views here.
