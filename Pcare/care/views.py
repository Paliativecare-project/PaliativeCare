from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'care/index.html')
def services(request):
    return render(request,'care/services.html')
def contact(request):
    return render(request,'care/contact.html')