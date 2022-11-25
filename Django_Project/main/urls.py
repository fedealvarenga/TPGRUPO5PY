"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#falta archivo views.py
from .views import *
urlpatterns = [
    path('cal/', cal),
    path('cal/<int:month>', cal),
    path('cal/<month>/', cal_prev, name = "cal_prev"),
    path('cal/<month>/', cal_next , name = "cal_next"),
    
    path('login/', login),
    path('hf/', header_footer),
]
