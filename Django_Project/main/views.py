from django.http import HttpResponse 
from django.template import Template, Context, loader_tags
from django.shortcuts import render
from .models import Database
import calendar  
import datetime

today = datetime.datetime.today()


def cal(request):
    date = datetime.datetime.today()   
    cal = calendar.monthcalendar(date.year, date.month)
    # redireccionar con lista despegable
    return render(request, "calendar.html", {"cal": cal, "year": date.year ,"month": date.strftime('%B'), "num": date.day, "today": date.strftime('%A')})

def calendar_next(request, month):
    # ver que pasa al pasar de year
    date = datetime.date(year=today.year, month=month+1, day=1)  
    cal = calendar.monthcalendar(date.year, month)
    # redireccionar con lista despegable
    return render(request, "calendar.html", {"cal": cal, "year": date.year ,"month": date.strftime('%B'), "t_day": today.day, "t_month": today.month})

def calendar_prev(request):
    # ver que pasa al pasar de year
    date = datetime.date(year=today.year, month=today.month-1, day=1)  
    cal = calendar.monthcalendar(date.year, date.month)
    # redireccionar con lista despegable
    return render(request, "calendar.html", {"cal": cal, "year": date.year ,"month": date.strftime('%B'), "num": date.day})


def login(request): #redireccion sign_up
    return render(request, "login.html")

def header_footer(request): #redireccion sign_up
    return render(request, "header_footer.html")