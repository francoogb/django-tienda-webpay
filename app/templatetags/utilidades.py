from django import template
from django.template import Context
from datetime import datetime, date
from django.contrib.sites.shortcuts import get_current_site
import os
from app.models import *




register = template.Library()


#################BASE DE DATOS
@register.filter(name='getCuantosItemsHayEnElCarrito')
def getCuantosItemsHayEnElCarrito(users_metadata_id):
    cuantos=Carrito.objects.filter(users_metadata_id=users_metadata_id).count()
    if cuantos==0:
        return ""
    elif cuantos==1:
        return f""" <span class='badge bg-dark text-white ms-1 rounded-pill' id='lblCartCount'>{cuantos}</span> <div>ítem</div>"""
    else:
        return f""" <span class='badge bg-dark text-white ms-1 rounded-pill' id='lblCartCount'>{cuantos}</span> <div>ítems</div>"""


 


@register.filter(name='getMetadata')
def getMetadata(n):
    datos=Metadata.objects.get()
    lista=[datos.keyword, datos.description, datos.correo, datos.telefono]
    if n==1:
        return datos.keyword
    if n==2:
        return datos.description
    if n==3:
        return datos.correo
    if n==4:
        return datos.telefono
    if n==5:
        return datos.nombre


#################FIN BASE DE DATOS
@register.filter(name='multiplicarValores')
def multiplicarValores(valor1, valor2):
    return valor1*valor2


@register.filter(name='diferenciaDiasFecha')
def diferenciaDiasFecha(fechaDateTime):
    fecha = fechaDateTime.strftime('%Y-%m-%d')
    fechaArray=fecha.split('-')
    future_date = date(int(fechaArray[0]), int(fechaArray[1]), int(fechaArray[2]))
    today = date.today()
    remaining_days = (today - future_date).days
    return f"{remaining_days}"


@register.filter(name='baseUrl')
def baseUrl(request):
    return f"http://{request.get_host()}"





@register.filter(name='numberFormat')
def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return "{:,}".format(numero).replace(",",".")


@register.filter(name='calculaEdad')
def calculaEdad(naci):
    import datetime
    hoy = datetime.date.today()
    if hoy < naci:
        return "error"
    else:
        ano = naci.year
        mes = naci.month
        dia = naci.day
 
        fecha = naci
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)
 
        #print ('Mi edad es: %s' % (edad-1))
        return edad-1


@register.filter(name='rutaActiva')
def rutaActiva(request, slug):
    path = request.path[1:len(request.path)].split('/')
    if path[0] == '':
        css = ''
    else:
        if path[0] == slug:
            css =f"active"
        else:
            css = ""
    return f'{css}'

 

 


@register.filter(name='invierteFecha')
def invierteFecha(fechaDateTime):
    fecha = fechaDateTime.strftime('%d/%m/%Y')
    return fecha


@register.filter(name='mesDeFecha')
def mesDeFecha(fechaDateTime):
    fecha = fechaDateTime.strftime('%Y-%m-%d')
    fechaArray=fecha.split('-')
    mes=''
    if fechaArray[1] =='01':
        mes = 'Enero'
    elif fechaArray[1] =='02':
        mes = 'Febrero'
    elif fechaArray[1] =='03':
        mes = 'Marzo'
    elif fechaArray[1] =='04':
        mes = 'Abril'
    elif fechaArray[1] =='05':
        mes = 'Mayo'
    elif fechaArray[1] =='06':
        mes = 'Junio'
    elif fechaArray[1] =='07':
        mes = 'Julio'
    elif fechaArray[1] =='08':
        mes = 'Agosto'
    elif fechaArray[1] =='09':
        mes = 'Septiembre'
    elif fechaArray[1] =='10':
        mes = 'Octubre'
    elif fechaArray[1] =='11':
        mes = 'Noviembre'
    elif fechaArray[1] =='12':
        mes = 'Diciembre'
    return f'{mes}/{fechaArray[0]}'


@register.filter(name='invierteFechaHora')
def invierteFechaHora(fechaDateTime):
    fecha = fechaDateTime.strftime('%d-%m-%Y %H:%M:%S')
    return fecha

@register.filter(name='getNombreMes')
def getNombreMes(numero):
    mes=''
    if numero ==1:
        mes = 'Enero'
    elif numero ==2:
        mes = 'Febrero'
    elif numero ==3:
        mes = 'Marzo'
    elif numero ==4:
        mes = 'Abril'
    elif numero ==5:
        mes = 'Mayo'
    elif numero ==6:
        mes = 'Junio'
    elif numero ==7:
        mes = 'Julio'
    elif numero ==8:
        mes = 'Agosto'
    elif numero ==9:
        mes = 'Septiembre'
    elif numero ==10:
        mes = 'Octubre'
    elif numero ==11:
        mes = 'Noviembre'
    elif numero ==12:
        mes = 'Diciembre'
    return f'{mes}'


@register.filter(name='formateaFechaActual')
def formateaFechaActual(fecha):#2020-08-04
    fechaDateTime = date.today()
    fecha = fechaDateTime.strftime('%Y-%m-%d')
    fechaArray=fecha.split('-')
    objeto_datetime = datetime.strptime(fecha, "%Y-%m-%d")
    dia_semana=datetime.weekday(objeto_datetime)
    
    if dia_semana==0:
        dia="Lunes"
    elif dia_semana==1:
        dia="Martes"
    elif dia_semana==2:
        dia="Miércoles"
    elif dia_semana==3:
        dia="Jueves"
    elif dia_semana==4:
        dia="Viernes"
    elif dia_semana==5:
        dia="Sábado"
    elif dia_semana==6:
        dia="Domingo"
    
        
    mes=''
    if fechaArray[1] =='01':
        mes = 'Enero'
    elif fechaArray[1] =='02':
        mes = 'Febrero'
    elif fechaArray[1] =='03':
        mes = 'Marzo'
    elif fechaArray[1] =='04':
        mes = 'Abril'
    elif fechaArray[1] =='05':
        mes = 'Mayo'
    elif fechaArray[1] =='06':
        mes = 'Junio'
    elif fechaArray[1] =='07':
        mes = 'Julio'
    elif fechaArray[1] =='08':
        mes = 'Agosto'
    elif fechaArray[1] =='09':
        mes = 'Septiembre'
    elif fechaArray[1] =='10':
        mes = 'Octubre'
    elif fechaArray[1] =='11':
        mes = 'Noviembre'
    elif fechaArray[1] =='12':
        mes = 'Diciembre'
    return f'{dia} {fechaArray[2]} de {mes} de {fechaArray[0]}'


@register.filter(name='formateaFecha')
def formateaFecha(fechaDateTime):#2020-08-04
    fecha = fechaDateTime.strftime('%Y-%m-%d')
    fechaArray=fecha.split('-')
    objeto_datetime = datetime.strptime(fecha, "%Y-%m-%d")
    dia_semana=datetime.weekday(objeto_datetime)
    
    if dia_semana==0:
        dia="Lunes"
    elif dia_semana==1:
        dia="Martes"
    elif dia_semana==2:
        dia="Miércoles"
    elif dia_semana==3:
        dia="Jueves"
    elif dia_semana==4:
        dia="Viernes"
    elif dia_semana==5:
        dia="Sábado"
    elif dia_semana==6:
        dia="Domingo"
    
        
    mes=''
    if fechaArray[1] =='01':
        mes = 'Enero'
    elif fechaArray[1] =='02':
        mes = 'Febrero'
    elif fechaArray[1] =='03':
        mes = 'Marzo'
    elif fechaArray[1] =='04':
        mes = 'Abril'
    elif fechaArray[1] =='05':
        mes = 'Mayo'
    elif fechaArray[1] =='06':
        mes = 'Junio'
    elif fechaArray[1] =='07':
        mes = 'Julio'
    elif fechaArray[1] =='08':
        mes = 'Agosto'
    elif fechaArray[1] =='09':
        mes = 'Septiembre'
    elif fechaArray[1] =='10':
        mes = 'Octubre'
    elif fechaArray[1] =='11':
        mes = 'Noviembre'
    elif fechaArray[1] =='12':
        mes = 'Diciembre'
    return f'{dia} {fechaArray[2]} de {mes} de {fechaArray[0]}'


@register.filter(name='formateaFecha')
def formateaFecha(fechaDateTime):#2020-08-04
    fecha = fechaDateTime.strftime('%Y-%m-%d')
    fechaArray=fecha.split('-')
    objeto_datetime = datetime.strptime(fecha, "%Y-%m-%d")
    dia_semana=datetime.weekday(objeto_datetime)
    
    if dia_semana==0:
        dia="Lunes"
    elif dia_semana==1:
        dia="Martes"
    elif dia_semana==2:
        dia="Miércoles"
    elif dia_semana==3:
        dia="Jueves"
    elif dia_semana==4:
        dia="Viernes"
    elif dia_semana==5:
        dia="Sábado"
    elif dia_semana==6:
        dia="Domingo"
    
        
    mes=''
    if fechaArray[1] =='01':
        mes = 'Enero'
    elif fechaArray[1] =='02':
        mes = 'Febrero'
    elif fechaArray[1] =='03':
        mes = 'Marzo'
    elif fechaArray[1] =='04':
        mes = 'Abril'
    elif fechaArray[1] =='05':
        mes = 'Mayo'
    elif fechaArray[1] =='06':
        mes = 'Junio'
    elif fechaArray[1] =='07':
        mes = 'Julio'
    elif fechaArray[1] =='08':
        mes = 'Agosto'
    elif fechaArray[1] =='09':
        mes = 'Septiembre'
    elif fechaArray[1] =='10':
        mes = 'Octubre'
    elif fechaArray[1] =='11':
        mes = 'Noviembre'
    elif fechaArray[1] =='12':
        mes = 'Diciembre'
    return f'{dia} {fechaArray[2]} de {mes} de {fechaArray[0]}'


@register.filter(name='formateaMesActual')
def formateaMesActual(numero):#2020-08-04
    fechaDateTime = date.today()
    fecha = fechaDateTime.strftime('%Y-%m-%d')
    fechaArray=fecha.split('-')
    numero = fechaArray[1]
    mes=''
    if numero =='01':
        mes = 'Enero'
    elif numero =='02':
        mes = 'Febrero'
    elif numero =='03':
        mes = 'Marzo'
    elif numero =='04':
        mes = 'Abril'
    elif numero =='05':
        mes = 'Mayo'
    elif numero=='06':
        mes = 'Junio'
    elif numero =='07':
        mes = 'Julio'
    elif numero =='08':
        mes = 'Agosto'
    elif numero =='09':
        mes = 'Septiembre'
    elif numero =='10':
        mes = 'Octubre'
    elif numero =='11':
        mes = 'Noviembre'
    elif numero =='12':
        mes = 'Diciembre'
    return f'{mes}/{fechaArray[0]}'