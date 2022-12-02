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
from django.urls import include, path

from .views import *

calendarpatterns = [
    path('', parque, name='parque'),
    path('cal/prev/', cal_prev),
    path('cal/next/', cal_next),
    path('cal/', cal),
    path('form_pago/<int:y>/<int:m>/<int:d>', form_pago, name='pago'),
]

urlpatterns = [
    path('', home, name='Home'),
    path('cal/prev/', cal_prev),
    path('cal/next/', cal_next),
    path('cal/', cal),

    path('login/', login),
    path('login/signup/', signup),
    path('login/user/', login_user),

    path('profile/', profile),
    path('profile/user/', modify_user),  

    path('test/', test),
    path('form_pago/<int:y>/<int:m>/<int:d>', form_pago, name='pago'),
    path('<str:nombre>/', include(calendarpatterns)),
    

]

