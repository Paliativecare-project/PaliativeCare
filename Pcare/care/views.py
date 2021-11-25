from django.shortcuts import render

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
    return render(request,'care/adminlogin.html')
def adminlogin(request):
    return render(request,'care/adminlogin.html')
def adminhome(request):
    return render(request,'care/adminhome.html')
    

def register(request):
    return render(request,'care/user_reg.html')

