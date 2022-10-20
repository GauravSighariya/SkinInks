from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contact-us/',views.contact,name='blog-contact')
    
]