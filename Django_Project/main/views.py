from django.http import HttpResponse 
from django.template import Template, Context, loader_tags
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Database
import calendar  
import datetime

today = datetime.datetime.today()
track_year = today.year

def cal(request, month = today.month):
    global track_year
    track_year = today.year
    cal = calendar.monthcalendar(today.year, month)
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
    if request.method == "POST":
        Mail = request.POST["Email"]
        Apellido = request.POST["Apellido"]
        Nombre = request.POST["Nombre"]
        Password = request.POST["Password"]

        db = Database()
        db.add_user(Apellido, Mail, Nombre, Password)
        return redirect(login)
    else:
        return redirect(login)

def login_user(request): 
    if request.method == "POST":

        Mail = request.POST["Email"]
        Password = request.POST["Password"]

        db = Database()
        person = db.get_user_bymail(Mail)
        track_user = person
        if person == tuple() :
            return redirect(login)
        elif person[0][4] == Password:
            return redirect(home) ## poner datos de factura
        else:
            return redirect(login)
    else:
        return redirect(login)

def modify_user(request): 
    if request.method == "POST":
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
    else:
        return redirect(profile)


def test(request):
    db = Database()
    date = datetime.date(2022, 12, 4)
    count = db.get_normal_tickets(date = date , parque = "Magic Kingdom")
    return HttpResponse(f"normal = {count[0][0]}")

#capacity[0][0] -> normal
#capacity[0][1] -> fast
def form_pago(request, y, m, d):
    db = Database()
    date = datetime.date(y, m, d)
    capacity = db.get_capacity(parque = "Magic Kingdom")
    count_n = db.get_normal_tickets(date = date , parque = "Magic Kingdom")
    count_f = db.get_fast_tickets(date = date , parque = "Magic Kingdom")
    count_f = count_f[0][0]
    count_n = count_n[0][0]

    date = datetime.date(y, m, d)
    return HttpResponse(f"fecha = {date} \n normal = {count_n} \n fast = {count_f} \n capacidad del dia \n fp: {capacity[0][1] - count_f} \n normal: {capacity[0][0] - count_n} ")

def parque(request, nombre):
    #return HttpResponse(f"{nombre}")
    return redirect(f"/{nombre}/cal")

