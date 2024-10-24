import os
from os import remove
import shutil
from pathlib import Path
from datetime import datetime, date, timedelta
from django.conf import settings
from app.models import *

RUTA=settings.RUTA
RUTA2=settings.RUTA2



def moverArchivoProducto(file, id):
    if existeArchivoMedia(file)==True:
        fecha = datetime.now()
        nombre = f"{datetime.timestamp(fecha)}{os.path.splitext(str(file))[1]}"
        shutil.move(f'{RUTA}tienda/media/{file}', f'{RUTA2}static/upload/producto/{nombre}')
        Producto.objects.filter(pk=id).update(foto=nombre)

 


def moverArchivoProducto2(file):
    shutil.move(f'{RUTA}tienda/media/producto/{file}', f'{RUTA2}static/upload/producto/{file}')


 
def moverArchivoProductoGaleria(file, id):
    if existeArchivoMedia(file)==True:
        fecha = datetime.now()
        nombre = f"{datetime.timestamp(fecha)}{os.path.splitext(str(file))[1]}"
        shutil.move(f'{RUTA}tienda/media/{file}', f'{RUTA2}static/upload/producto/{nombre}')
        ProductoFotos.objects.filter(pk=id).update(foto=nombre)

def existeArchivo(carpeta, archivo):
    try:
        ruta = f"{RUTA}/tienda/static/upload/{carpeta}/{archivo}"
        fileObj = Path(ruta)
        existe = fileObj.is_file()
        print(f"Existe en '{carpeta}': {existe}")
        return existe
    except Exception as e:
        print(f"No existe en '{carpeta}' (con error)")
        return False


def existeArchivoMedia(archivo):
    try:
        ruta = f"{RUTA}tienda/media/{archivo}"
        fileObj = Path(ruta)
        existe = fileObj.is_file()
        print(f"Existe en 'media': {existe}")
        return existe
    except Exception as e:
        print("No existe en 'media' (con error)")
        return False
