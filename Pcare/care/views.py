from django.shortcuts import render,redirect,HttpResponse
from django.http.response import HttpResponse
from .models import Addservice
from .models import Adminlogin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'care/index.html')
def services(request):
    return render(request,'care/services.html')
def contact(request):
    return render(request,'care/contact.html')
def about(request):
    return render(request,'care/about.html')

def adminlogin(request):
    if request.method == 'POST':
        a_name=request.POST.get('a_name')
        a_password=request.POST.get('a_password')
        
        user=Adminlogin.objects.filter(a_name=a_name,a_password=a_password).first()
        
        if user is not None:
            
            return redirect("adminhome")
           
        else: 
            messages.success(request,"Username or password is incorrect") 
    context={}        
    
    return render(request,'care/adminlogin.html',context)
      
            
#def adminlogin(request):
#     return render(request,'care/adminlogin.html')
def adminhome(request):
    return render(request,'care/adminhome.html')
def adminservice(request):
    if request.method == 'POST':
        s_name=request.POST['s_name']
        obj=Addservice()
        obj.s_name=s_name
        obj.save()
        messages.info(request,"Service Added")
    else:
        pass 
    return render(request,'care/adminservice.html')
def adminedit(request):
    item_list=Addservice.objects.all()
    context={
        'item_list' : item_list
    }
    return render(request,'care/adminedit.html',context)
def adminverify(request):
    return render(request,'care/adminverify.html')   

def register(request):
    return render(request,'care/user_reg.html')
def login(request):
    return render(request,'care/Service_login.html')

