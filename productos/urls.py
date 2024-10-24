from django.urls import path
from .views import *

urlpatterns = [
	path('detalle/<int:id>/<str:slug>', productos_detalle, name="productos_detalle"),
]