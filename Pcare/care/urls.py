from django.urls import path
from . import views
from care.views import update,delete
urlpatterns = [
    path('',views.index,name="home"),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    
    

    path('adminlogin/',views.adminlogin, name="adminlogin"),

    path('adminhome/',views.adminhome, name="adminhome"),
    path('adminservice/',views.adminservice,name="adminservice"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_reg/',views.user_reg,name="user_reg"),
    
    path('login/',views.login,name="servicelogin"),
     path('service_reg/',views.service_reg,name="service_reg"),
    path('adminverify/',views.adminverify,name="adminverify"),
    path('adminedit/',views.adminedit,name="adminedit"),
    path('update/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),
    path('logout/',views.logout_view,name="logout"),
    ]
