from django.http import HttpResponse 
from django.template import Template, Context, loader_tags
from django.shortcuts import render
from .models import Database
import calendar  
import datetime

today = datetime.datetime.today()


def cal(request, month = today.month):
    date = datetime.datetime.today()   
    cal = calendar.monthcalendar(date.year, month)
    # redireccionar con lista despegable
    return render(request, "calendar.html", {"cal": cal, "year": date.year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month })

def cal_next(request):
    # ver que pasa al pasar de year
    month = request.GET.get('month')
    cal(request, month+1)

def cal_prev(request, month):
    # ver que pasa al pasar de year
    month = request.GET.get('month')
    cal(request, month-1)
    
def login(request): #redireccion sign_up
    return render(request, "login.html")

def header_footer(request): #redireccion sign_up
    return render(request, "header_footer.html")