from django.urls import path
from .views import *

urlpatterns = [
	path('login', acceso_login, name="acceso_login"),
	path('registro', acceso_registro, name="acceso_registro"),
	path('verificacion/<str:token>', acceso_verificacion, name="acceso_verificacion"),
	path('reset', acceso_reset, name="acceso_reset"),
	path('restore/<str:token>', acceso_restore, name="acceso_restore"),
	path('salir', acceso_salir, name="acceso_salir"),
]