from django.urls import path
from . import views                 #importing views in current application using dot

urlpatterns =[
    path('',views.home)             #mapping views.home function 
]