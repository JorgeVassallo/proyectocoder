from django import forms

class SucursalesFormulario(forms.Form):
    direccion = forms.CharField(max_length=35)
    telefono = forms.CharField(max_length=35)
    provincia = forms.CharField(max_length=35)

class SaboresFormulario(forms.Form):
    sabor = forms.CharField(max_length=25)
    ingredientes = forms.CharField(max_length=150)
    disponibilidad = forms.BooleanField(required=False)

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    direccion = forms.CharField(max_length=35)
    telefono = forms.CharField(max_length=35)
    email = forms.EmailField()

class EmpleadosFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    dni = forms.CharField(max_length=35)

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()