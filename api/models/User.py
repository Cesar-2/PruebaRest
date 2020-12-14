from django.db import models


class User(models.Model):
    name = models.CharField("Nombre", max_length=200)
    last_name = models.CharField("Apellido", max_length=200)
    document = models.CharField("Identificacion", max_length=11)
    email = models.CharField("Correo electronico", max_length=200)
    password = models.CharField("Contraseña", max_length=200)


class Metadata:
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"


def __str__(self):
    return "{} - {}".format(self.pk, self.email)
