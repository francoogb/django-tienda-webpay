from datetime import datetime, date, timedelta

from django.conf import settings
import os
from os import remove
from urllib.parse import urlparse, parse_qs
from django.core.paginator import Paginator
from django.template import Context, Template
#token
import jwt
import time
#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def getToken(json):
    token= jwt.encode(json, settings.SECRET_KEY, algorithm='HS256')
    return token


def traducirToken(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])


def sendMail(html, asunto, para):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = asunto
    msg['From'] = settings.MAIL_SALIDA
    msg['To'] = para

    msg.attach(MIMEText(html, 'html'))
    
    try:
        # Configuración del servidor SMTP
        server = smtplib.SMTP(settings.SERVER_STMP, settings.PUERTO_SMTP)
        server.starttls()
        server.login(settings.MAIL_SALIDA, settings.PASSWORD_MAIL_SALIDA)

        # Envía el correo
        server.sendmail(settings.MAIL_SALIDA, para, msg.as_string())

        # Cierra la conexión con el servidor SMTP
        server.quit()

    except smtplib.SMTPException as e:
        # Maneja la excepción general de SMTP
        print(f"Error al enviar el correo: {e}")

    except Exception as e:
        # Puedes manejar otras excepciones específicas si es necesario
        print(f"Otro tipo de error: {e}")


def getExtension(file):
    extension = os.path.splitext(str(file))[1]
    if extension == ".png":
        return True
    elif extension == ".jpg":
        return True
    elif extension == ".jpeg":
        return True
    elif extension == ".JPG":
        return True
    elif extension == ".PNG":
        return True
    elif extension == ".JPEG":
        return True
    else:
        return False


def paginacion(total, request):
    paginator = Paginator(total, settings.TOTAL_PAGINAS)
    page = request.GET.get('page')
    datos = paginator.get_page(page)
    numeros=[]
    if len(datos)>=settings.TOTAL_PAGINAS:
        for ultima in range(1, datos.paginator.num_pages):
            numeros.append(ultima)
        numeros.append(ultima+1)
    return [datos, numeros, page]


def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return "{:,}".format(numero).replace(",",".")