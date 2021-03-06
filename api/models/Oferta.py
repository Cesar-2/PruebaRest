from django.db import models


class Oferta(models.Model):
    name = models.CharField("Nombre", max_length=200)
    store = models.ForeignKey('api.Tienda', on_delete=models.CASCADE)
    image = models.CharField("Imagen", max_length=200)
    price = models.IntegerField("Precio")


class Metadata:
    verbose_name = "Trato"
    verbose_name_plural = "Tratos"


def __str__(self):
    return "{} - {}".format(self.pk, self.name)
