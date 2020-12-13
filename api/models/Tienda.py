from django.db import models


class TiendaAPI(models.Model):
    brand = models.ForeignKey('Marca', on_delete=models.CASCADE)
    identifier = models.CharField("Identificador", max_length=200)
    name = models.CharField("Nombre", max_length=200)
    thumbnail = models.CharField("Icono", max_length=200)
    address = models.CharField("Direccion", max_length=200)


class Medadato:
    verbose_name = "Tienda"
    verbose_name_plural = "Tiendas"


def __str__(self):
    return "{} - {}".format(self.pk, self.name)