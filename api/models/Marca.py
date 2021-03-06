from django.db import models


class Marca(models.Model):
    name = models.CharField("Nombre", max_length=200)
    logo = models.CharField("Logo", max_length=200)


class Metadata:
    verbose_name = "Marca"
    verbose_name_plural = "Marcas"


def __str__(self):
    return "{} - {}".format(self.pk, self.name)
