"""LearningGateway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Dashboard import views as dash_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Dashboard.urls')),                                  #added app url path
    path('register/',dash_views.register,name='register'),                      #register url
    path('login/',auth_views.LoginView.as_view(template_name ="Dashboard/login.html"),name='login'),  
    path('profile/',dash_views.profile,name='profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name ="Dashboard/logout.html"),name='logout'),     
]
