from django.shortcuts import render,redirect
from.models import MyInfo            # import 'models.py' for store data into database


def data (request):
    mydata = MyInfo.objects.all()     # here retrive all data for show in webpage
    if(mydata!=''):
        return render(request,'sql_front.html',{'datas':mydata})
    else:
        return render(request, "sql_front.html")

def adata(request):           #  <!--adata mean add data-->
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
        return redirect('data')         # here 'data' name is from { app urls file('urls.py') } file name redirect to data page
    return render(request, "sql_front.html")

def udata(request, id):    # Here using id for getting values <!--udata mean update data-->
    mydata = MyInfo.objects.get(id=id)    # Here get data from table'MyInfo'
    if request.method == "POST":
        Name = request.POST['name']    # Here get data from html file  # then Name is varible to sotre value of 'name' from html file
        Age = request.POST['age']      # Here get data from html file 
        Address = request.POST['address']   # Here get data from html file 
        Phone = request.POST['phone']       # Here get data from html file 

        mydata.name=Name
        mydata.age=Age
        mydata.address=Address
        mydata.phone=Phone
        mydata.save()

        return redirect('data')
        
    return render(request, 'udata.html',{'data':mydata})

def ddata(request, id):   #<!--ddata mean delete data-->
    mydata = MyInfo.objects.get(id=id)    # Here get data from table'MyInfo'
    mydata.delete()
    return redirect('data')  # Here using 'data' is a home url 

# Create your views here.
