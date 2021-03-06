# Generated by Django 3.1.4 on 2020-12-13 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('logo', models.CharField(max_length=200, verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200, verbose_name='Identificador')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('thumbnail', models.CharField(max_length=200, verbose_name='Icono')),
                ('address', models.CharField(max_length=200, verbose_name='Direccion')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('image', models.CharField(max_length=200, verbose_name='Imagen')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tienda')),
            ],
        ),
    ]
