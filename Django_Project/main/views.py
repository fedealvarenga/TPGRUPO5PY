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


def signup(request):
    """   if request.method == "POST":

        data = request.POST
    """
    Mail = request.GET["Email"]
    Apellido = request.GET["Apellido"]
    Nombre = request.GET["Nombre"]
    Password = request.GET["Password"]

    db = Database()
    db.add_user(Apellido, Mail, Nombre, Password)
    return render(request, "login.html")

def login_user(request): 
    global track_user
    Mail = request.GET["Email"]
    Password = request.GET["Password"]

    db = Database()
    person = db.get_user_bymail(Mail)
    track_user = person
    if person == tuple() :
        return redirect("/login/")
    elif person[0][4] == Password:
        track_user = person[0]
        return redirect("/")
    else:
        return redirect("/login/")

def modify_user(request): 
    Mail = request.GET["Email"]
    Password = request.GET["Password"]
    new_Nombre = request.GET["new_Nombre"]
    new_Apellido = request.GET["new_Apellido"]
    new_Password = request.GET["new_Password"]

    db = Database()
    person = db.get_user_bymail(Mail)
    if person[0][4] == Password:
        db.modify_user(new_Apellido, new_Nombre, new_Password, Mail)
        return render(request, "home.html")

def profile(request):
    return render(request, "profile.html")

def test(request):
    return render(request, "test.html", {"user": track_user})