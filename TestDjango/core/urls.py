from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index,crearproveedor,modificarproveedor,eliminarproveedor,verproveedor

urlpatterns = [
    path ('',index, name="index"), 
    path('verproveedor', verproveedor, name="verproveedor"),
    path('crearproveedor', crearproveedor, name="crearproveedor"),
    path('modificarproveedor/<id>', modificarproveedor, name="modificarproveedor"),
    path('eliminarproveedor/<id>', eliminarproveedor, name="eliminarproveedor"),
]
    