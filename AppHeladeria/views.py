from django.shortcuts import render
from django.http import HttpResponse
from AppHeladeria.models import *
from AppHeladeria.forms import *

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "inicio.html", {"mensaje": "Bienvenido a mi heladeria"})

def acerca_de_mi(request):

    return render(request, "about.html", {"mensaje": "Bienvenido a mi heladeria"})

# Iniciar sesion
    
def iniciar_sesion(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            info_dic = formulario.cleaned_data #se convierte en diccionario

            usuario = authenticate(username=info_dic["username"], password=info_dic["password"])

            if usuario is not None:

                login(request, usuario)

                return render(request, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            
            else:

                return render(request, "inicio.html", {"mensaje": "ERROR AL INICIAR SESION"})
    else:

        formulario = AuthenticationForm()
    
    return render(request, "inicio_sesion.html", {"formu": formulario})

# Registrarse

def registrarse(request):

    if request.method == "POST":

        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            return render(request, "inicio.html", {"mensaje":"El usuario ha sido creado con exito."})
        
    else:

        formulario = UserCreationForm()

    return render(request, "registro.html", {"formu":formulario})

# Agregar avatar

@login_required
def agregar_avatar(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            
            info = formulario.cleaned_data
            usuario_actual = User.objects.get(username=request.user)

            nuevo_avatar = Avatar(usuario=usuario_actual, imagen=info["imagen"])

            nuevo_avatar.save()

            return render(request, "inicio.html", {"mensaje":"Has creado un nuevo avatar."})
        
    else:

        formulario = AvatarFormulario()

    return render(request, "nuevo_avatar.html", {"formu":formulario})

@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario =  EditarUsuario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.username = informacion["username"]

            usuario.save()

            return render(request, "inicio.html")
    else:
        miFormulario = EditarUsuario(initial={'username': usuario.username,
                                             'email': usuario.email})


    return render(request, "editar_usuario.html", {"formu": miFormulario})



def cerrar_sesion(request):

    logout(request)

    return render(request, "inicio.html", {"mensaje":"Has cerrado sesion con exito"})



# CRUD de los modelos

# CRUD de sucursales

@login_required
def crear_sucursal(request):

    if request.method == "POST":
        sucursal_formulario = SucursalesFormulario(request.POST) # se almacena la info del form
        if sucursal_formulario.is_valid():
            sucursal_dic = sucursal_formulario.cleaned_data #se convierte en diccionario

            sucursal_nueva = Sucursales(direccion=sucursal_dic["direccion"], 
                                        telefono=sucursal_dic["telefono"], 
                                        provincia=sucursal_dic["provincia"]
                                        )
            sucursal_nueva.save()
            return render(request, "inicio.html")
    else:

        sucursal_formulario = SucursalesFormulario()

    return render(request, "crear_sucursal.html", {"formu": sucursal_formulario})


def ver_sucursales(request):

    todas_sucursales = Sucursales.objects.all()

    return render(request, "ver_sucursales.html", {"total": todas_sucursales})


@login_required
def actualizar_sucursales(request, sucursal_info):

    sucursal_elegida = Sucursales.objects.get(id=sucursal_info)

    if request.method == "POST":
        sucursal_formulario = SucursalesFormulario(request.POST) # se almacena la info del form
        if sucursal_formulario.is_valid():
            sucursal_dic = sucursal_formulario.cleaned_data #se convierte en diccionario

            #Actualizamos la info
            sucursal_elegida.direccion = sucursal_dic["direccion"]
            sucursal_elegida.telefono = sucursal_dic["telefono"]
            sucursal_elegida.provincia = sucursal_dic["provincia"]

            sucursal_elegida.save()

            return render(request, "inicio.html")
    else:

        sucursal_formulario = SucursalesFormulario(initial={"direccion": sucursal_elegida.direccion, 
                                                            "telefono": sucursal_elegida.telefono, 
                                                            "provincia": sucursal_elegida.provincia}
                                                            )

    return render(request, "actualizar_sucursales.html", {"formu": sucursal_formulario})

@login_required
def borrar_sucursal(request, sucursal_info):

    sucursal_elegida = Sucursales.objects.get(id=sucursal_info)

    sucursal_elegida.delete()

    return render(request, "inicio.html")

# CRUD de clientes

@login_required
def crear_cliente(request):

    if request.method == "POST":
        cliente_formulario = ClientesFormulario(request.POST) # se almacena la info del form
        if cliente_formulario.is_valid():
            cliente_dic = cliente_formulario.cleaned_data #se convierte en diccionario

            cliente_nuevo = Clientes(nombre=cliente_dic["nombre"], 
                                        apellido=cliente_dic["apellido"], 
                                        direccion=cliente_dic["direccion"],
                                        telefono=cliente_dic["telefono"],
                                        email=cliente_dic["email"]
                                        )
            cliente_nuevo.save()
            return render(request, "inicio.html")
    else:

        cliente_formulario = ClientesFormulario()
    
    return render(request, "crear_cliente.html", {"formu": cliente_formulario})

@login_required
def ver_clientes(request):

    todos_clientes = Clientes.objects.all()

    return render(request, "ver_clientes.html", {"total": todos_clientes})

@login_required
def borrar_cliente(request, cliente_info):

    cliente_elegido = Clientes.objects.get(id=cliente_info)

    cliente_elegido.delete()

    return render(request, "inicio.html")


@login_required
def actualizar_clientes(request, cliente_info):

    cliente_elegido = Clientes.objects.get(id=cliente_info)

    if request.method == "POST":
        cliente_formulario = ClientesFormulario(request.POST) # se almacena la info del form
        if cliente_formulario.is_valid():
            cliente_dic = cliente_formulario.cleaned_data #se convierte en diccionario

            #Actualizamos la info
            cliente_elegido.nombre = cliente_dic["nombre"]
            cliente_elegido.apellido = cliente_dic["apellido"]
            cliente_elegido.direccion = cliente_dic["direccion"]
            cliente_elegido.telefono = cliente_dic["telefono"]
            cliente_elegido.email = cliente_dic["email"]

            cliente_elegido.save()

            return render(request, "inicio.html")
    else:

        cliente_formulario = ClientesFormulario(initial={"nombre": cliente_elegido.nombre, 
                                                            "apellido": cliente_elegido.apellido, 
                                                            "direccion": cliente_elegido.direccion,
                                                            "telefono": cliente_elegido.telefono,
                                                            "email": cliente_elegido.email}
                                                            )

    return render(request, "actualizar_clientes.html", {"formu": cliente_formulario})


# CRUD de Sabores

@login_required
def crear_sabores(request):
    if request.method == "POST":
        sabores_formulario = SaboresFormulario(request.POST) # se almacena la info del form
        if sabores_formulario.is_valid():
            sabores_dic = sabores_formulario.cleaned_data #se convierte en diccionario

            sabor_nuevo = Sabores(sabor=sabores_dic["sabor"], 
                                        ingredientes=sabores_dic["ingredientes"], 
                                        disponibilidad=sabores_dic["disponibilidad"]
                                        )
            sabor_nuevo.save()
            return render(request, "inicio.html")
    else:

        sabores_formulario = SaboresFormulario()
    
    return render(request, "crear_sabores.html", {"formu": sabores_formulario})


def ver_sabores(request):

    todos_sabores = Sabores.objects.all()

    return render(request, "ver_sabores.html", {"total": todos_sabores})

@login_required
def actualizar_sabores(request, sabor_info):

    sabor_elegido = Sabores.objects.get(sabor=sabor_info)

    if request.method == "POST":
        sabor_formulario = SaboresFormulario(request.POST) # se almacena la info del form
        if sabor_formulario.is_valid():
            sabor_dic = sabor_formulario.cleaned_data #se convierte en diccionario

            #Actualizamos la info
            sabor_elegido.sabor = sabor_dic["sabor"]
            sabor_elegido.ingredientes = sabor_dic["ingredientes"]
            sabor_elegido.disponibilidad = sabor_dic["disponibilidad"]

            sabor_elegido.save()

            return render(request, "inicio.html")
    else:

        sabor_formulario = SaboresFormulario(initial={"sabor": sabor_elegido.sabor, 
                                                            "ingredientes": sabor_elegido.ingredientes, 
                                                            "disponibilidad": sabor_elegido.disponibilidad}
                                                            )

    return render(request, "actualizar_sabores.html", {"formu": sabor_formulario})


def ver_empleados(request):

    todos_empleados = Empleados.objects.all()

    return render(request, "ver_empleados.html", {"total": todos_empleados})





@login_required
def borrar_sabores(request, sabor_info):

    sabor_elegido = Sabores.objects.get(sabor=sabor_info)

    sabor_elegido.delete()

    return render(request, "inicio.html")



# CRUD empleados

@login_required
def crear_empleado(request):
    if request.method == "POST":
        empleado_formulario = EmpleadosFormulario(request.POST) # se almacena la info del form
        if empleado_formulario.is_valid():
            empleado_dic = empleado_formulario.cleaned_data #se convierte en diccionario

            empleado_nuevo = Empleados(nombre=empleado_dic["nombre"], 
                                        apellido=empleado_dic["apellido"], 
                                        dni=empleado_dic["dni"]
                                        )
            empleado_nuevo.save()
            return render(request, "inicio.html")
    else:

        empleado_formulario = EmpleadosFormulario()
    
    return render(request, "crear_empleados.html", {"formu": empleado_formulario})


@login_required
def actualizar_empleados(request, empleado_info):

    empleado_elegido = Empleados.objects.get(id=empleado_info)

    if request.method == "POST":
        empleado_formulario = EmpleadosFormulario(request.POST) # se almacena la info del form
        if empleado_formulario.is_valid():
            empleado_dic = empleado_formulario.cleaned_data #se convierte en diccionario

            #Actualizamos la info
            empleado_elegido.nombre = empleado_dic["nombre"]
            empleado_elegido.apellido = empleado_dic["apellido"]
            empleado_elegido.dni = empleado_dic["dni"]

            empleado_elegido.save()

            return render(request, "inicio.html")
    else:

        empleado_formulario = EmpleadosFormulario(initial={"nombre": empleado_elegido.nombre, 
                                                            "apellido": empleado_elegido.apellido, 
                                                            "dni": empleado_elegido.dni}
                                                            )

    return render(request, "actualizar_empleados.html", {"formu": empleado_formulario})


@login_required
def borrar_empleado(request, empleado_info):

    empleado_elegido = Empleados.objects.get(id=empleado_info)

    empleado_elegido.delete()

    return render(request, "inicio.html")





# Busquedas

@login_required
def buscar_cliente(request):

    if request.GET:
        nombre = request.GET["nombre"]
        cliente = Clientes.objects.filter(nombre__icontains=nombre)

        mensaje = f"Buscando cliente {nombre}"  

        return render(request, "buscar_cliente.html", {"mensaje":mensaje, "resultado":cliente})
    
    return render(request, "buscar_cliente.html")

@login_required
def buscar_sucursal(request):

    if request.GET:
        direccion = request.GET["direccion"]
        sucursal = Sucursales.objects.filter(direccion__icontains=direccion)

        mensaje = f"Buscando sucursal {direccion}"  

        return render(request, "buscar_sucursal.html", {"mensaje":mensaje, "resultado":sucursal})
    
    return render(request, "buscar_sucursal.html")

@login_required
def buscar_sabor(request):

    if request.GET:
        sabor = request.GET["sabor"]
        saborbusqueda = Sabores.objects.filter(sabor__icontains=sabor)

        mensaje = f"Buscando sabor {sabor}"  

        return render(request, "buscar_sabor.html", {"mensaje":mensaje, "resultado":saborbusqueda})
    
    return render(request, "buscar_sabor.html")

@login_required
def buscar_empleados(request):

    if request.GET:
        empleado = request.GET["dni"]
        empleadobusqueda = Empleados.objects.filter(dni__icontains=empleado)

        mensaje = f"Buscando empleado {empleado}"  

        return render(request, "buscar_empleados.html", {"mensaje":mensaje, "resultado":empleadobusqueda})
    
    return render(request, "buscar_empleados.html")



class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiar_contra.html"
    success_url = "/AppHeladeria/"