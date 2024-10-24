from django.shortcuts import render
from app.models import *


def productos_detalle(request, id, slug):
    try:
        datos = Producto.objects.filter(pk=id, slug=slug, estado_id=1).get()
    except Producto.DoesNotExist:
        raise Http404

    # Impresiones de depuración
    print("ID:", id)
    print("Slug:", slug)

    relacionados = Producto.objects.filter(estado_id=1, producto_categoria=datos.producto_categoria_id).filter(estado_id=1).all()
    fotos = ProductoFotos.objects.filter(producto_id=id).all()
    
    return render(request, 'productos/detalle.html', {'datos': datos, 'relacionados': relacionados, 'fotos': fotos})
