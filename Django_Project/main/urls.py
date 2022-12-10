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
from django.urls import include, path, register_converter

from .views import *

class FloatUrlParameterConverter:
    regex = '[0-9]+\.?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

register_converter(FloatUrlParameterConverter, 'float')

calendarpatterns = [
    path('<str:park_str>', cal, name='calendar'),
    path('<str:park_str>/prev/', cal_prev, name='calendar_prev'),
    path('<str:park_str>/next/', cal_next, name='calendar_next'),
]


urlpatterns = [
    path('', home, name='home'),
    path('filter/', filter_view, name='filter_view'),
    path('filter_disney/', filter_disney, name='filter_disney'),
    path('cal/', include(calendarpatterns)), 
    

    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('signup/action', button_signup, name='button_signup'),
    path('login/user/', login_user),
    path('login/user_id:<int:id_user>/facturas/', facturas, name='facturas'),

    path('profile/', profile, name='profile'),
    path('profile/user/', modify_user, name='modify_user'),  

    path('test/', test),
    path('form_pago/<str:park_str>/<int:y>/<int:m>/<int:d>', form_pago, name='pago'),
    path('form_pago/buy/', add_ticket, name='buy'), 
    path('pdf/<int:id_f>/<str:name>/<float:tot>', create_pdf, name='pdf'),


    path('<str:park>/', parque, name='parque'),     
]

