from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from app.models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, date, timedelta
from utilidades import utilidades
import time
from django.conf import settings
from django.contrib.auth.hashers import make_password
from slugify import slugify


def acceso_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = Formulario_Login(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            correo = request.POST['correo']
            password = request.POST['password']
            user = authenticate(request, username=correo, password=password)
            if user is not None:
                login(request, user)
                usersMetadata = UsersMetadata.objects.filter(user_id=request.user.id).get()
                request.session['users_metadata_id'] =  usersMetadata.id
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.WARNING, f'Los datos ingresados no son correctos, por favor vuelva a intentar.')
                return HttpResponseRedirect('/acceso/login')
    return render(request, 'acceso/login.html', {'form': form})


def acceso_registro(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = Formulario_Registro(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            existe=User.objects.filter(username=request.POST['correo']).count()
            if existe !=0:
                mensaje = f"El E-Mail ingresado ya está siendo usado por otro usuario, por favor intente con otro."
                messages.add_message(request, messages.WARNING, mensaje)
                return HttpResponseRedirect('/acceso/registro')
            ahora=datetime.now()
            fecha= datetime.strptime(f"{ahora.year}-{ahora.month}-{ahora.day}", "%Y-%m-%d")
            nombre=f"{request.POST['nombre']}-{request.POST['apellido']}"
            u=User.objects.create_user(username = request.POST['correo'], password = request.POST['password'], email = request.POST['correo'], first_name=request.POST['nombre'], last_name=request.POST['apellido'], is_active=0)
            UsersMetadata.objects.create(correo=request.POST['correo'], telefono='', direccion='', estado_id=2, pais_id=1, perfiles_id=1, user_id=u.id, genero_id=3, slug = slugify(nombre))
            token=utilidades.getToken({'id': u.id, 'time':int(time.time())})
            #token='123455'
            url=f"{settings.BASE_URL}acceso/verificacion/{token}"
            html=f"""Hola {request.POST['nombre']} {request.POST['apellido']}, te has registrado correctamente en www.tienda.com. Estás a punto de completar tu registro, por favor haz clic en el siguiente enlace para terminar el proceso, o cópialo y pégalo en la barra de direcciones de tu navegador favorito:
                    <br />
                    <br />
                    <a href="{url}">{url}</a>
                """
            utilidades.sendMail(html, 'Tienda', request.POST['correo'])
            mensaje = f"Se creó el registro exitosamente. Se ha enviado un mail a {request.POST['correo']} para activar tu cuenta."
            messages.add_message(request, messages.SUCCESS, mensaje)
            return HttpResponseRedirect('/acceso/registro')
        else:
            mensaje = f"No fué posible crear el registro, por favor vuelva a intentarlo"
            messages.add_message(request, messages.WARNING, mensaje)
            return HttpResponseRedirect('/acceso/registro')
    return render(request, 'acceso/registro.html', {'form': form})


def acceso_verificacion(request, token):
    token=utilidades.traducirToken(token)
    fecha = datetime.now()
    despues = fecha + timedelta(days=1)
    fecha_numero=int(datetime.timestamp(despues))
    if fecha_numero>token['time']:
        try:
            
            UsersMetadata.objects.filter(user_id=token['id']).filter(estado_id=2).get()
            User.objects.filter(pk=token['id']).update(is_active=1)
            UsersMetadata.objects.filter(user_id=token['id']).update(estado_id=1)
            mensaje = f"Se activó tu cuenta exitosamente, ahora ya puedes participar de nuestros contenidos. Te invitamos a loguearte y completar tu perfil, para que podamos conocernos mejor."
            messages.add_message(request, messages.SUCCESS, mensaje)
            return HttpResponseRedirect('/acceso/login')
        except UsersMetadata.DoesNotExist:
            raise Http404
    else:
        raise Http404


def acceso_restore(request, token):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    token_original=token
    token=utilidades.traducirToken(token)
    fecha = datetime.now()
    despues = fecha + timedelta(days=1)
    fecha_numero=int(datetime.timestamp(despues))
    if fecha_numero>token['time']:
        form = Formulario_Restore(request.POST or None)
        if request.method =='POST':
            if form.is_valid():
                try:
                    user=UsersMetadata.objects.filter(user_id=token['id']).get()
                    if request.POST['password1'] != request.POST['password2']:
                        
                        mensaje = f"Las contraseñas ingresadas no coinciden"
                        messages.add_message(request, messages.WARNING, mensaje)
                        return HttpResponseRedirect('/acceso/reset')
                    else:
                        User.objects.filter(id=token['id']).update(password=make_password(request.POST['password1']))
                        mensaje = f"Se ha restablecido tu contraseña exitosamente, ahora ya puedes loguearte de nuevo y disfrutar de todos nuestros cursos. No olvides no compartir tu contraseña con nadie."
                        messages.add_message(request, messages.SUCCESS, mensaje)
                        return HttpResponseRedirect('/acceso/login')
                except UsersMetadata.DoesNotExist:
                    raise Http404
        return render(request, 'acceso/restore.html', {'form': form, 'token':token_original})
    else:
        raise Http404


def acceso_reset(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = Formulario_Reset(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            try:
                user=UsersMetadata.objects.filter(correo=request.POST['correo']).get()
                token=utilidades.getToken({'id': user.user_id, 'time':int(time.time())})
                url=f"{settings.BASE_URL}acceso/restore/{token}"
                html=f"""Hola {user.user.first_name} {user.user.last_name}, has solicitado recuperar tu contraseña, por motivos de seguridad te enviamos el siguiente enlace para terminar el proceso, o cópialo y pégalo en la barra de direcciones de tu navegador favorito:
                    <br />
                    <br />
                    <a href="{url}">{url}</a>
                """
                utilidades.sendMail(html, 'Tienda', request.POST['correo'])
                mensaje = f"Se ha enviado un mail a {request.POST['correo']} con las instrucciones para activar tu cuenta."
                messages.add_message(request, messages.SUCCESS, mensaje)
                return HttpResponseRedirect('/acceso/reset')
            except UsersMetadata.DoesNotExist:
                mensaje = f"El E-Mail {request.POST['correo']} no corresponde a ninguno de nuestros usuarios."
                messages.add_message(request, messages.WARNING, mensaje)
                return HttpResponseRedirect('/acceso/reset')
    return render(request, 'acceso/reset.html', {'form': form})


def acceso_salir(request):
    logout(request)
    try:
        del request.session['users_metadata_id']
    except KeyError:
        pass
    messages.add_message(request, messages.WARNING, f'Se cerró la sesión exitosamente.')
    return HttpResponseRedirect('/acceso/login')


