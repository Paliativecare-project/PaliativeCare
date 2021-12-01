from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),

    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('adminhome/',views.adminhome, name="adminhome"),
    path('adminservice/',views.adminservice,name="adminservice"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="servicelogin"),
    path('adminverify/',views.adminverify,name="adminverify"),
    path('adminedit/',views.adminedit,name="adminedit"),
    
    ]
