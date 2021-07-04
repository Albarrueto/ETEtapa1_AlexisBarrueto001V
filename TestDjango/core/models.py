from django.db import models

# Create your models here.


class Pais(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='ID País')
    nombrepais = models.CharField(max_length=50, verbose_name='Nombre país')

    def __str__(self):
        return self.nombrepais

class Moneda(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='ID Moneda')
    tipomoneda = models.CharField(max_length=50, verbose_name='Tipo moneda(Pesos/Dólares)')

    def __str__(self):
        return self.tipomoneda

class Proveedor(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='Numero de identificación')
    nombrecompleto = models.CharField(max_length=50, verbose_name='Nombre completo')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    direccion = models.CharField(max_length=30, verbose_name='Dirección')
    email = models.EmailField(max_length=50, verbose_name='E-mail')    
    contrasena = models.CharField(max_length=20, verbose_name='Contraseña')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)    
    def __str__(self):
        return self.id,self.nombrecompleto
