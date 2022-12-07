from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, loader_tags
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import resolve, reverse
from .models import Database
from pdf_module.pdf import make_pdf
import os
import calendar  
import datetime

today = datetime.datetime.today()
track_year = today.year

def cal(request, park_str):
    global track_year
    month = today.month
    track_year = today.year
    cal = calendar.monthcalendar(today.year, month)
    return render(request, "calendar.html", {"cal": cal, "year": today.year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year, "park": park_str})

def cal_next(request, park_str):
    global track_year

    month = int(request.GET['month'])+1 
    if month == 13:
        track_year = track_year+1
        month = 1
        cal = calendar.monthcalendar(track_year, month)
        return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year, "park": park_str})
        
    cal = calendar.monthcalendar(track_year, month)
    return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year, "park": park_str})
    

def cal_prev(request, park_str):
    global track_year
   
    # ver que pasa al pasar de year
    month = int(request.GET['month'])-1 
    if month == 0:
        track_year = track_year-1
        month = 12
        cal = calendar.monthcalendar(track_year, month)
        return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year, "park": park_str})
        
    cal = calendar.monthcalendar(track_year, month)
    return render(request, "calendar.html", {"cal": cal, "year": track_year ,"month_name": calendar.month_name[month], "today_day_number": today.day, "today_month_number": today.month , "actual_month_number": month, "today_year": today.year, "park": park_str})
    
def login(request): 
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request, "profile.html")

def buttom_signup(request):
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

def signup(request):
    return render(request, "signup.html")

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
            #return redirect(facturas) ## poner datos de factura
            return HttpResponseRedirect(reverse('facturas', args=(person[0][0],)))
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
def form_pago(request, y, m, d, park_str):
    db = Database()
    date = datetime.date(y, m, d)
    capacity = db.get_capacity(parque = park_str)
    count_n = db.get_normal_tickets(date = date , parque = park_str)
    count_f = db.get_fast_tickets(date = date , parque = park_str)
    count_f = count_f[0][0]
    count_n = count_n[0][0]

    # Calculo la capacidad de entradas normales
    normal_capacity=capacity[0][0] - count_n
    # Calculo la capacidad de entradas fastpass
    fastpass_capacity=capacity[0][1] - count_f

    date = datetime.date(y, m, d)
    
    #cambio el return HttprResponse por el render (aunque lo dejo comentado por las dudas)
    return render(request,"buy.html", {"name_park":park_str,"travel_year":date.year,"travel_month":date.month,"travel_day":date.day,"n_tickets": range(0, normal_capacity+1) ,"fp_tickets": range(0, fastpass_capacity+1)})
    
    #return HttpResponse(f"Parque = {park_str} \n fecha = {date} \n normal = {count_n} \n fast = {count_f} \n capacidad del dia \n fp: {capacity[0][1] - count_f} \n normal: {capacity[0][0] - count_n} ")

def parque(request, park):
    return HttpResponseRedirect(reverse('calendar', args=(park,)))


def add_ticket(request):
    PRICE_FAST = 1000
    PRICE_NORMAL = 500 
    if request.method == "POST":
        dtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        park_name = request.POST["Park"]
        date= request.POST["t_date"]
        normal = int(request.POST.getlist("lista_normal")[0])
        fast = int(request.POST.getlist("lista_fastpass")[0])

        Mail = request.POST["Email"]
        Password = request.POST["Password"]

        db = Database()
        person = db.get_user_bymail(Mail)
        
        if person == tuple() :
            return redirect(add_ticket)
        elif person[0][4] == Password:
            id_user = person[0][0]

            total = normal*(PRICE_NORMAL) + fast*(PRICE_FAST)

            if normal == 0 and fast == 0:
                return redirect(home)
            if normal != 0 or fast != 0:
                db.add_factura(id_user, dtime, total)
                id_factura = db.get_factura(id_user, dtime)[0][0]
            if normal != 0:
                for i in range(normal):
                    db.insert_ticket(1, id_user, id_factura, park_name, date)
            if fast != 0:
                for i in range(fast):
                    db.insert_ticket(2, id_user, id_factura, park_name, date)
        
        return HttpResponseRedirect(reverse('pdf', args=(id_factura, person[0][1], total)))
        ##return redirect(success)
    else:
        return redirect(home)


class User:
    def __init__ (self, user):
        self.id_user = user[0]
        self.nombre = user[1]
        self.apellido = user[2]
        self.mail = user[3]

    def __str__ (self):
        return f"{self.id_user} // {self.nombre} // {self.apellido}  // {self.mail}"

class Factura:
    def __init__ (self, factura):
        self.id_factura = factura[0]
        self.fk_user = factura[1]
        self.dtime = factura[2]
        self.total = factura[3]

    def __str__ (self):
        return f"{self.id_factura} // {self.fk_user} // {self.dtime}  // {self.total}"

def facturas(request, id_user):
    #return render(request, "facturas.html")
    db = Database()
    facturas = db.get_all_facturas(id_user)
    user = db.get_user_byid(id_user)[0]

    lista_facturas = list()
    for x in facturas:
        lista_facturas.append(Factura(x))

    user = User(user)

    #return HttpResponse(f"{lista_facturas[0]}")

    return render(request,"facturas.html", {"user": user, "facturas": lista_facturas, 'i': 0})


def create_pdf(request, id_f, name, tot):
    db = Database()
    n = db.get_data_normal(id_f)
    f = db.get_data_fast(id_f)
    date_entradas = db.get_data_fecha(id_f)
    park = db.get_data_park(id_f) 
    date_factura = db.get_data_fecha_factura(id_f)

    pdf_path = make_pdf(titular = name, n = n, f = f, date_factura = date_factura, date_entradas = date_entradas, park = park, total = tot, data_in = id_f)

## retornar PDF
    #return HttpResponse(f"{name} // n:{n} // f:{f} // date:{date_entradas} // park: {park} // total:{tot} // compra = {date_factura} ") 

    with open(f'{pdf_path}', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline;filename={date_factura}_{tot}.pdf'
        #os.remove(f'{pdf_path}')
        return response

