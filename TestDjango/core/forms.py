from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Pais, Moneda, Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta: 
        model= Proveedor
        fields = ['id', 'nombrecompleto', 'telefono', 'direccion', 'email', 'contrasena', 'pais', 'moneda']
        labels ={
            'id': 'ID', 
            'nombrecompleto': 'Nombre', 
            'telefono': 'Teléfono', 
            'direccion': 'Dirección',
            'email': 'E-mail',
            'contrasena': 'Contraseña',
            'pais': 'País',
            'moneda': 'Moneda',
        }
        widgets={
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ID', 
                    'id': 'id'
                }
            ), 
            'nombrecompleto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre completo', 
                    'id': 'nombrecompleto'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese teléfono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese dirección', 
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese e-mail', 
                    'id': 'email'
                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contrasena'
                }
            ),
            'pais': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'pais',
                }
            ),
            'moneda': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'moneda',
                }
            )

        }