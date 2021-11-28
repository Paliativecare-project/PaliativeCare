from django.shortcuts import render
from .models import Addservice
from .models import Adminlogin
from django.contrib.auth import authenticate
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
        username=request.POST['username']
        password=request.POST['password'] 
        check_if_user_exists = Adminlogin.objects.filter(yourtablefield="username").exists()
        if check_if_user_exists:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            return ('adminhome')
            
    else:    
        return render(request,'care/adminlogin.html')
def adminlogin(request):
    return render(request,'care/adminlogin.html')
def adminhome(request):
    return render(request,'care/adminhome.html')
def adminservice(request):
    if request.method == 'POST':
        s_name=request.POST['s_name']
        obj=Addservice()
        obj.s_name=s_name
        obj.save()
    return render(request,'care/adminservice.html')
def adminverify(request):
    return render(request,'care/adminverify.html')   

def register(request):
    return render(request,'care/user_reg.html')
def login(request):
    return render(request,'care/Service_login.html')
