from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm


def index(request):
    return render(request, 'index.html')



def crearproveedor(request):
    if request.method=='POST': 
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('verproveedor')
    else:
        proveedor_form= ProveedorForm()
    return render(request, 'core/form_crear_proveedor.html', {'proveedor_form': proveedor_form})


def verproveedor(request):
    proveedores = Proveedor.objects.all()

    return render(request, 'core/verproveedor.html', context={'proveedores':proveedores})


def modificarproveedor(request,id):
    proveedor = Proveedor.objects.get(id=id)

    datos ={
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()           
            return redirect('verproveedor')
    return render(request, 'core/modificarproveedor.html', datos)


def eliminarproveedor(request,id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect('verproveedor')