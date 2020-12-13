from django.db import models


class ProductoAPI(models.Model):
    name = models.CharField("Nombre", max_length=200)
    store = models.ForeignKey('Tienda', on_delete=models.CASCADE)
    image = models.CharField("Imagen", max_length=200)
    price = models.CharField("Precio")


class Medadato:
    verbose_name = "Trato"
    verbose_name_plural = "Tratos"


def __str__(self):
    return "{} - {}".format(self.pk, self.name)
