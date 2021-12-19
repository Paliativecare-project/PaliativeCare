from django import template
from django.shortcuts import render,redirect,HttpResponse
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import Addservice, Users,Servicesmodel
from .models import Adminlogin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import TodoForm
from django.contrib.auth.models import User,auth
from django.core.mail import EmailMessage
from django.conf import Settings, settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.views import View
from .forms import *
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

    if request.method == 'POST':
        u_email=request.POST.get('u_email')
        u_password=request.POST.get('u_password')
        
        user=Users.objects.filter(u_email=u_email,u_password=u_password).first()
        
        if user is not None:
            
            return redirect("userhome")
           
        else: 
            messages.success(request,"Username or password is incorrect") 
    context={}        
    
    return render(request,'care/user_login.html',context)
      
            
    #return render(request,'care/user_login.html')
def user_reg(request):
    if request.method=='POST':
        u_name=request.POST['u_name']
        u_email=request.POST['u_email']
        u_phn=request.POST['u_phn']
        u_address=request.POST['u_address']
        u_password=request.POST['u_password']
        obj1=Users()
        obj1.u_name=u_name
        obj1.u_email=u_email
        obj1.u_phn=u_phn
        obj1.u_address=u_address
        obj1.u_password=u_password
        obj1.save()
        return render(request,'care/user_login.html')
    else:
        pass

        

    return render(request,'care/user_reg.html')

def userhome(request):
    return render(request,'care/userhome.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')
#def user_reg(request): 

  #  return render(request,'care/user_reg.html')
def service_reg(request):
    if request.method=='POST':
        name=request.POST['name']
        s_license=request.POST['s_license']
        phn=request.POST['phn']
        addr=request.POST['addr']
        distric=request.POST['distric']
        password=request.POST['password']
        pincode=request.POST['pincode']
        email=request.POST['email']
        obj2=Servicesmodel()
        obj2.name=name
        obj2.email=email
        obj2.phn=phn
        obj2.addr=addr
        obj2.password=password
        obj2.s_license=s_license
        obj2.distric=distric
        obj2.pincode=pincode
        obj2.save()
        return render(request,'care/Service_login.html')
    else:
        pass
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
    item_list=Servicesmodel.objects.all()
    context={
        'item_list' : item_list
    }
    return render(request,'care/adminverify.html',context)   



def login(request): 
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        status=request.POST.get('status')
        user=Servicesmodel.objects.filter(email=email,password=password,status=1).first()
        
        if user is not None:
            return redirect("sevicehome")  
        else: 
            messages.success(request,"Username or password is incorrect OR you are not approved by Admin") 
    context={}        
    
    return render(request,'care/Service_login.html',context)
def sevicehome(request):
    return render(request,'care/sevicehome.html')
   # return render(request,'care/Service_login.html')

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
def delete1(request,id):
    if request.method == 'POST':
        Servicesmodel.objects.get(id=id).delete()
        return redirect('adminverify')
def approve(request,id):
    if request.method == 'POST':
        t=Servicesmodel.objects.get(id=id)
        t.status=True
        t.save()
        #return redirect('adminverify')
    #template=render_to_string('care/email_template.html',{'name':request.Servicesmodel.name})
    subject='Welcome to Caring Hands'
    msg = ("%s %s %s" % ("Hai ",t.name,",  You are approved by Admin.'"))
    send_mail(
        subject,
        msg,
        'techsupport@teqstories.com',
        [t.email],
        fail_silently=False,
    )
    
    
    # email_from=settings.EMAIL_HOST_USER
    # recipient_list=[Servicesmodel.email,]
    # EmailMessage(subject,message,email_from,recipient_list)
    return redirect('adminverify')
    #email.fail_silently=False
    #email.send()
def logout_view(request):
    logout(request)
    return redirect('adminlogin')
def logout_s(request):
    logout(request)
    return redirect('Service_login')


class AddServiceView(View):
    def get(self, request):
        user = request.user
        print(user)
        form = AddServiceForm()
        context = {'form': form}
        return render(request,'care/add_service.html',context)

    def post(self, request):
        user = request.user
        form = AddServiceForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.provider = user
            f.save()

            

    



        
