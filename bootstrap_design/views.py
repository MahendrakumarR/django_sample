from django.shortcuts import render


def boot(request):
    return render(request, "boot.html")

def boot_out(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    phone = request.POST.get('phone')
    return render(request, 'boot_out.html', {'name':name, 'age':age, 'phone':phone})
# Create your views here.
