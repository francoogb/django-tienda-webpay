from functools import wraps
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages


def logueado():
    def _activo_required(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.add_message(request, messages.WARNING, 'Debes estar logueado para visualizar este contenido.')
                return HttpResponseRedirect('/acceso/login')
            else:
                return func(request, *args, **kwargs)
        return _decorator
    return _activo_required


def acceso_empresa():
    def _activo_required(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            if request.session['perfiles_id'] == 1:
                return func(request, *args, **kwargs)
            else:
                raise Http404
        return _decorator
    return _activo_required