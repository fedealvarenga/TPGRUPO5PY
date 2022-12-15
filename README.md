# TPGRUPO5
<div align="center" style="display:flex;justify-content:center; align-items:center;">
  <img src="https://user-images.githubusercontent.com/82116673/206872926-aee27e4e-f319-4f85-bf59-bcec101e9347.png" width="200"/>
  <img src="https://user-images.githubusercontent.com/82116673/206872959-be82a2bc-c779-49a3-a7d5-2100dd00c0d1.png" width="200"/>
</div>

<div align="center">

![HTML5](https://img.shields.io/badge/-HTML5-000000?style=flat&logo=html5&logoColor=white)
![Css](https://img.shields.io/badge/css-black?logo=CSS%20Wizardry&logoColor=white&style=flat)
![BootStrap](https://img.shields.io/badge/BOOTSTRAP-black?logo=bootstrap&logoColor=white&style=flat)
![Python](https://img.shields.io/badge/PYTHON-black?logo=python&logoColor=white&style=flat)
![Mysql](https://img.shields.io/badge/MYSQL-black?logo=mysql&logoColor=white&style=flat)
![Django](https://img.shields.io/badge/DJANGO-black?logo=django&logoColor=white&style=flat)

</div>

# Idea 
El eje del proyecto es realizar una página web que permita Crear, Leer, Modificar y Borrar usuarios (CRUD) con una base de datos. Además se implementa con la reserva de tickets y la generación de una factura que incluye QR en formato PDF.

## Futuras implementaciones 

* Leer el Código QR para permitir el acceso y uso de la entrada. 
  
* Optimizar la implementación de Django, es decir, utilizar el ORM que proporciona el entorno de desarrollo en vez de utilizar MySQL 'por fuera' del entorno.

# Installation

```bash
git clone https://github.com/fedealvarenga/TPGRUPO5PY.git

cd TPGRUPO5PY

pip install -r requirements.txt
```

## Packages used 

```bash
  fpdf==1.7.2
  Pillow==9.0.1
  qrcode==7.3.1
  imutils==0.5.4
  cryptography==3.4.8
  PyMySQL==1.0.2
  opencv-python==4.6.0.66
  requests==2.28.1
  Django==4.1.3
```


# Link MySQL

Para utilizar la aplicación hay que 'instalar' la base de datos propuesta por el archivo `Proyecyto_DB_DEV.sql`. 

Luego, se modifican las credenciales de acceso en el bloque `__init__(self)` de la `class Database()` en el archivo: *TPGRUPO5PY/Django_Project/main/models.py*

```python
user = 'YOUR MySQL user'
password = 'YOUR MySQL password'
```

# Use Django
Para usar un proyecto existente se requieren las siguientes líneas de código:

```bash
cd Django_Project

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Para visualizar la aplicación, ingresar en un navegador:  [localhost:8000/](http://localhost:8000/)


# Contacto

<div align='center'>

  * > Alvarenga Federico
    * falvarenga@frba.utn.edu.ar
    * federico.alvarenga@hotmail.com

  <br>

  * > Borello Federico
    * fborello@frba.utn.edu.ar
    * federico.borello@hotmail.com
    
  <br>

  * > Golfieri Zoe
    * Gzoe@frba.Utn.edu.ar
    * ZoeGolfieri02@gmail.com

  <br>

  * > Palazzo Cristian
    * cpalazzo@frba.utn.edu.ar
    * cristianpalazzo14@gmail.com

  <br>

  * > Vega Ramon
    * rvegabaldiviezo@frba.utn.edu.ar
    * rvegabaldiviezo@gmail.com

</div>

# Usage

![GIF](Capgemini.gif)
  

