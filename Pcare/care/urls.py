from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact")
]
