from django.urls import path
from . import views                 #importing views in current application using dot

urlpatterns =[
    path('',views.home, name="home") ,            #mapping views.home function 
    path('notes',views.notes,name="notes")       #mapping views.notes function
]