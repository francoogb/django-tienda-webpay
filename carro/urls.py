from django.urls import path
from .views import *

urlpatterns = [
	path('', carro_inicio, name="carro_inicio"),
	path('crear', carro_crear, name="carro_crear"),
	path('vaciar', carro_vaciar, name="carro_vaciar"),
	path('quitar-de-carro/<int:id>', carro_quitar, name="carro_quitar"),
	path('modificar-cantidad-carro/<int:id>/<int:cantidad>', carro_modificar_cantidad, name="carro_modificar_cantidad"),
	path('pagar', carro_pagar, name="carro_pagar"),
	path('webpay', carro_webpay, name="carro_webpay"),
	path('webpay-respuesta', carro_webpay_respuesta, name="carro_webpay_respuesta"),
]