from django.urls import path
from AppHeladeria.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("about/", acerca_de_mi, name="About"),

    path("login/", iniciar_sesion, name="Iniciar Sesion"),
    path("signup/", registrarse, name="Registrarse"),
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),
    path("edit/", editar_usuario, name="Editar Usuario"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contra"),
    path("avatar/", agregar_avatar, name="Agregar Avatar"),

    path("crear_empleado/", crear_empleado, name="Crear_empleado"),
    path("ver_empleados/", ver_empleados, name="ver_empleados"),
    path("buscar_empleados/", buscar_empleados, name="Buscar_empleados"),
    path("actualizar_empleados/<empleado_info>", actualizar_empleados, name="Actualizar_empleados"),
    path("borrar_empleado/<empleado_info>", borrar_empleado, name="Borrar_empleado"),

    
    path("crear_clientes/", crear_cliente, name="Crear_cliente"),
    path("ver_clientes/", ver_clientes, name="Clientes"),
    path("buscar_cliente/", buscar_cliente, name="Buscar_cliente"),
    path("actualizar_clientes/<cliente_info>", actualizar_clientes, name="Actualizar_clientes"),
    path("borrar_cliente/<cliente_info>", borrar_cliente, name="Borrar_cliente"),

    path("crear_sucursales/", crear_sucursal, name="Crear_sucursal"),
    path("buscar_sucursal/", buscar_sucursal, name="Buscar_sucursal"),
    path("ver_sucursales/", ver_sucursales, name="Sucursales"),
    path("actualizar_sucursales/<sucursal_info>", actualizar_sucursales, name="Actualizar_sucursales"),
    path("borrar_sucursal/<sucursal_info>", borrar_sucursal, name="Borrar_sucursal"),

    path("crear_sabores/", crear_sabores, name="Crear_sabores"),    
    path("buscar_sabor/", buscar_sabor, name="Buscar_sabor"),   
    path("ver_sabores/", ver_sabores, name="Sabores"),
    path("actualizar_sabores/<sabor_info>", actualizar_sabores, name="Actualizar_sabores"),
    path("borrar_sabores/<sabor_info>", borrar_sabores, name="Borrar_sabores"),
    
]