from django.shortcuts import render
from.models import MyInfo            # import 'models.py' for store data into database


def data (request):
    mydata = MyInfo.objects.all()     # here retrive all data for show in webpage
    return render(request, "sql_front.html")

def adata(request):
    if request.method =='POST':
        Name = request.POST['name']    # here get data from html file  # then Name is varible to sotre value of 'name' from html file
        Age = request.POST['age']      # here get data from html file 
        Address = request.POST['address']   # here get data from html file 
        Phone = request.POST['phone']       # here get data from html file 

        obj = MyInfo()                # 'obj' is object of 'MyInfo' class from 'models.py' file for pass data to sqlite database
        obj.name = Name           # here 'obj.name' is call the 'models.py' class variable 'name'
        obj.age = Age             # here 'obj.age' is call the 'models.py' class variable 'age'
        obj.address = Address     # here 'obj.address' is call the 'models.py' class variable 'address'
        obj.phone = Phone         # here 'obj.phone' is call the 'models.py' class variable 'phone'
        obj.save()                # here use 'save' for save all data into database
        mydata = MyInfo.objects.all()     # here retrive all data for show in webpage
        return render(request, "sql_front.html",{'datas':mydata})
    return render(request, "sql_front.html")

# Create your views here.
