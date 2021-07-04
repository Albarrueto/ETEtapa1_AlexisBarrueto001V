from django.contrib import admin
from .models import Pais, Moneda,   Proveedor
# Register your models here.

admin.site.register(Pais)
admin.site.register(Moneda)
admin.site.register(Proveedor)