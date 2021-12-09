from django.urls import path
from . import views
from care.views import update,delete,approve,delete1
urlpatterns = [
    path('',views.index,name="home"),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    
    

    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('adminhome/',views.adminhome, name="adminhome"),
    path('adminservice/',views.adminservice,name="adminservice"),
    path('login/',views.login,name="servicelogin"),
    path('service_reg/',views.service_reg,name="service_reg"),
    path('adminverify/',views.adminverify,name="adminverify"),
    path('adminedit/',views.adminedit,name="adminedit"),
    path('update/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),
    path('delete1/<int:id>/',delete1,name="delete1"),
    path('approve/<int:id>/',approve,name="approve"),
    path('logout/',views.logout_view,name="logout"),
    path('logout2/',views.logout_s,name="logout2"),
    path('logout1/',views.user_logout,name="logout1"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_reg/',views.user_reg,name="user_reg"),
    path('userhome/',views.userhome, name="userhome"),
    path('sevicehome/',views.sevicehome, name="sevicehome"),
    path('Service_login/',views.login, name="Service_login"),
    #path('user_logout/',views.user_logout,name="logout"),
    ]
