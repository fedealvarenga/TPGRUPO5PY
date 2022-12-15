from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.template import Template, Context, loader_tags
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.views.decorators import gzip
from .models import Database
from pdf_module.pdf import make_pdf
import os
import calendar  
import datetime
import threading
import cv2
import imutils
import numpy as np

import requests

url = 'https://api.apilayer.com/fixer/latest?symbols=ARS,BRL,EUR,GBP,CNY,UYU&base=USD&apikey=Hkh0nTZPyR3vU39anHzASmH2NLmANKyi'
response = requests.request("GET", url)
result = response.json()
usds = result['rates']['ARS']

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

def button_signup(request):
    if request.method == "POST":
        Mail = request.POST["Email"]
        Apellido = request.POST["Apellido"]
        Nombre = request.POST["Nombre"]
        Password = request.POST["Password"]

        db = Database()
        person = db.get_user_bymail(Mail)
        
        if person == tuple() :
            db.add_user(Apellido, Mail, Nombre, Password)
            return redirect(login)
        else:
            return redirect(signup)
    else:
        return redirect(home)

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
    
    return render(request,"buy.html", {"name_park":park_str,"travel_year":date.year,"travel_month":date.month,"travel_day":date.day,"n_tickets": range(0, normal_capacity+1) ,"fp_tickets": range(0, fastpass_capacity+1)})


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
    def __init__ (self, factura, usds):
        self.id_factura = factura[0]
        self.fk_user = factura[1]
        self.dtime = factura[2]
        self.total = factura[3]
        self.total_usd = float("{:.2f}".format(self.total/usds))

    def __str__ (self):
        return f"{self.id_factura} // {self.fk_user} // {self.dtime}  // {self.total}"

def facturas(request, id_user):
    db = Database()
    facturas = db.get_all_facturas(id_user)
    user = db.get_user_byid(id_user)[0]

    url = 'https://api.apilayer.com/fixer/latest?symbols=ARS,BRL,EUR,GBP,CNY,UYU&base=USD&apikey=Hkh0nTZPyR3vU39anHzASmH2NLmANKyi'
    response = requests.request("GET", url)
    result = response.json()
    usds = result['rates']['ARS']

    lista_facturas = list()
    for x in facturas:
        lista_facturas.append(Factura(x, usds))

    user = User(user)

    return render(request,"facturas.html", {"user": user, "facturas": lista_facturas, 'i': 0})


def create_pdf(request, id_f, name, tot):
    db = Database()
    n = db.get_data_normal(id_f)
    f = db.get_data_fast(id_f)
    date_entradas = db.get_data_fecha(id_f)
    park = db.get_data_park(id_f) 
    date_factura = db.get_data_fecha_factura(id_f)

    pdf_path = make_pdf(titular = name, n = n, f = f, date_factura = date_factura, date_entradas = date_entradas, park = park, total = tot, data_in = id_f)

    with open(f'{pdf_path}', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline;filename={date_factura}_{tot}.pdf'
        os.remove(f'{pdf_path}')
        return response


@gzip.gzip_page
def filter_disney(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    HttpResponse("ERROR")

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        frame = self.frame

        imagen = cv2.imread("../filtro/minnie.png", cv2.IMREAD_UNCHANGED)# me da 4 canales y el 4to es el fondo transparente del png
        # Detector de rostros
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        rostros = faceClassif.detectMultiScale(frame, 1.3, 5)

        for (x, y, w, h) in rostros:
            #redimenciono la imagen para que se adepte al rectangulo creado pro el rostro detectado
            imagen_redimensionada = imutils.resize(imagen, width=w)
            filas_image = imagen_redimensionada.shape[0]#shape me da una tupla con el tamaño del array
            #filas_image = imagen.shape[0]
            col_image = w
            # Agarro una parte de la cara para que la imagen no quede muy arriba
            porcion_alto = filas_image // 4
            dif = 0
            #Me fijo si la imagen entra en el video
            if y + porcion_alto - filas_image >= 0:
                pos_imagen = frame[y + porcion_alto - filas_image : y + porcion_alto,
                    x : x + col_image]
            else:
                #Calculo lo que sobrepasa la imagen el recuadro de la camara
                dif = abs(y + porcion_alto - filas_image) 
                pos_imagen = frame[0 : y + porcion_alto,
                    x : x + col_image]
            #Hago que la imagen no muestre el fondo blanco del png
            #Solo agarro el fondo de la imagen (lo pone en negro)
            fondo_imagen = imagen_redimensionada[:, :, 3]
            #invierto por lo tanto solo tomo la imagen que me interesa (en negro)
            fondo_imagen_inv = cv2.bitwise_not(fondo_imagen)
            #uno las 2 imagenes anteriores para formar la imagen pero con fondo negro y color
            fondo_negro = cv2.bitwise_and(imagen_redimensionada, imagen_redimensionada, mask=fondo_imagen)
            fondo_negro = fondo_negro[dif:, :, 0:3] #no tomo todos los canales de la imagen porq osino rompe
            #hago que el fondo negro sea transparente
            fondo_transparente = cv2.bitwise_and(pos_imagen,pos_imagen, mask=fondo_imagen_inv[dif:,:])
            # Sumamos las dos imágenes obtenidas
            imagen_filtro = cv2.add(fondo_negro, fondo_transparente)
            if y + porcion_alto - filas_image >= 0:
                frame[y + porcion_alto - filas_image : y + porcion_alto, x : x + col_image] = imagen_filtro

            else:
                frame[0 : y + porcion_alto, x : x + col_image] = imagen_filtro
        try:
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        except:
            frame = np.zeros((480,640,3), np.uint8)
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
            

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def filter_view(request):
    return render(request, 'filter.html')