from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput


class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete':'off'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete':'off'}))


class Formulario_Registro(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off'}))
    apellido = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete':'off'}))
    correo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete':'off'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete':'off'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir Contraseña', 'autocomplete':'off'}))


class Formulario_Reset(forms.Form):
    correo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete':'off'}))


class Formulario_Restore(forms.Form):
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir Contraseña'}))