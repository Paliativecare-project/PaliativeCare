from django.shortcuts import render,redirect,HttpResponse
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import Addservice
from .models import Adminlogin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import TodoForm
# Create your views here.
def index(request):
    return render(request,'care/index.html')
def services(request):
    return render(request,'care/services.html')
def contact(request):
    return render(request,'care/contact.html')
def about(request):
    return render(request,'care/about.html')

def user_login(request):
    return render(request,'care/user_login.html')
def user_reg(request): 
    return render(request,'care/user_reg.html')
def service_reg(request):
    return render(request,'care/service_reg.html')

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



def login(request):
    return render(request,'care/Service_login.html')

def update(request,id):
    context={}
    todo=Addservice.objects.get(id=id)
    form=TodoForm(instance=todo)
    if request.method == 'POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('adminedit')
    
    return render(request,'care/update.html',{'form':form})
def delete(request,id):
    if request.method == 'POST':
        Addservice.objects.get(id=id).delete()
        return redirect('adminedit')
def logout_view(request):
    logout(request)
    return redirect('adminlogin')
        
