# Generated by Django 3.2.3 on 2021-07-04 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='ID País')),
                ('tipomoneda', models.CharField(max_length=50, verbose_name='Tipo moneda(Pesos/Dólares)')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='ID País')),
                ('nombrepais', models.CharField(max_length=50, verbose_name='Nombre país')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Numero de identificación')),
                ('nombrecompleto', models.CharField(max_length=50, verbose_name='Nombre completo')),
                ('telefono', models.FloatField(max_length=10, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=30, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=20, verbose_name='E-mail')),
                ('contrasena', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.moneda')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
    ]