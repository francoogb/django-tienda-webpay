import requests
import json
import random
from django.conf import settings
from app.models import *
from utilidades import utilidades


def crearTransaccion(users_metadata_id, direccion, comuna_id):
	#se crea la orden de compra
	
	datos=Carrito.objects.filter(users_metadata_id=users_metadata_id).order_by('-id').all()
	suma=0
	for dato in datos:
		valor=dato.cantidad*dato.producto.precio
		suma=suma+valor
	
	try:
		orden=OrdenDeCompra.objects.filter(users_metadata_id=users_metadata_id, estado_id=3).get()
	except OrdenDeCompra.DoesNotExist:
		orden=OrdenDeCompra.objects.create(users_metadata_id=users_metadata_id, suma=suma, direccion=direccion, comuna_id=comuna_id, estado_id=3)

	buy_order = f"orden{orden.id}"
	session_id = str(random.randrange(1000000, 99999999))
	amount = suma
	ruta=f"{settings.BASE_URL}carro/webpay-respuesta"
	endpoint=settings.WEBPAY_URL
	payload={
		 "buy_order": buy_order,
		 "session_id": session_id,
		 "amount": amount,
		 "return_url": ruta
		}
	cabeceros = {'content-type': 'application/json', 'Tbk-Api-Key-Id': settings.WEBPAY_ID, 'Tbk-Api-Key-Secret': settings.WEBPAY_SECRET}
	response= requests.post(endpoint, json=payload, headers=cabeceros)
	#response.status_code
	respuesta=json.loads(response.text)
	#guardo el token recibido
	OrdenDeCompra.objects.filter(id=orden.id).update(token_ws=respuesta['token'])
	#retorno token y URL
	ruta=f"{respuesta['url']}{respuesta['token']}"
	return respuesta


def verificarTransaccion(token):
	endpoint=f"{settings.WEBPAY_URL}/{token}"
	cabeceros = {'content-type': 'application/json', 'Tbk-Api-Key-Id': settings.WEBPAY_ID, 'Tbk-Api-Key-Secret': settings.WEBPAY_SECRET}
	response= requests.put(endpoint, headers=cabeceros)
	#response.status_code
	respuesta=json.loads(response.text)
	if response.status_code ==200:
		return [respuesta['status'], respuesta['card_detail']['card_number'], respuesta['transaction_date']]
	else:
		return ['vacio']