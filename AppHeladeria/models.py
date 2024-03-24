from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    dni = models.CharField(max_length=35)

    def __str__(self):

        return f"{self.nombre}, {self.apellido}"


class Clientes(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    email = models.EmailField()

    def __str__(self):

        return f"{self.nombre}, {self.apellido}"

class Sabores(models.Model):
    sabor = models.CharField(max_length=25)
    ingredientes = models.CharField(max_length=150)
    disponibilidad = models.BooleanField()

    def __str__(self):

        return f"{self.sabor}"

class Sucursales(models.Model):
    direccion = models.CharField(max_length=35)
    telefono = models.CharField(max_length=35)
    provincia = models.CharField(max_length=35)

    def __str__(self):

        return f"{self.direccion}"
    
class EditarUsuario(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["username", "email"]

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)