from django.http import HttpResponse 
from django.template import Template, Context, loader_tags
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Database
import calendar  
import datetime

today = datetime.datetime.today()
track_year = today.year
track_user = tuple()

def cal(request, month = today.month):
    global track_year
    track_year = today.year
    cal = calendar.monthcalendar(today.year, month)
    # redireccionar con lista despegable
    return render(request, "calendar.html", {"cal": cal, "year": today.year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year })

def cal_next(request):
    global track_year

    month = int(request.GET['month'])+1 
    if month == 13:
        track_year = track_year+1
        month = 1
        cal = calendar.monthcalendar(track_year, month)
        return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year})
        
    cal = calendar.monthcalendar(track_year, month)
    return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year })
    

def cal_prev(request):
    global track_year
   
    # ver que pasa al pasar de year
    month = int(request.GET['month'])-1 
    if month == 0:
        track_year = track_year-1
        month = 12
        cal = calendar.monthcalendar(track_year, month)
        return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year })
        
    cal = calendar.monthcalendar(track_year, month)
    return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year })
    
def login(request): 
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")


def profile(request):
    return render(request, "profile.html")

def signup(request):
    Mail = request.POST["Email"]
    Apellido = request.POST["Apellido"]
    Nombre = request.POST["Nombre"]
    Password = request.POST["Password"]

    db = Database()
    db.add_user(Apellido, Mail, Nombre, Password)
    return redirect(login)

def login_user(request): 
    global track_user
    Mail = request.POST["Email"]
    Password = request.POST["Password"]

    db = Database()
    person = db.get_user_bymail(Mail)
    track_user = person
    if person == tuple() :
        return redirect(login)
    elif person[0][4] == Password:
        track_user = person[0]
        return redirect(home) ## poner datos de factura
    else:
        return redirect(login)

def modify_user(request): 
    Mail = request.POST["Email"]
    Password = request.POST["Password"]
    new_Nombre = request.POST["new_Nombre"]
    new_Apellido = request.POST["new_Apellido"]
    new_Password = request.POST["new_Password"]

    db = Database()
    person = db.get_user_bymail(Mail)
    if person == tuple() :
        return redirect(profile)
    elif person[0][4] == Password:
        db.modify_user(new_Apellido, new_Nombre, new_Password, Mail)
        return redirect(home)
    else:
        return redirect(profile)


def test(request):
    return render(request, "test.html", {"user": track_user})