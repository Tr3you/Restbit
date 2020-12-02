"""Restbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('crear_reservacion/', views.crear_reservacion, name='Crear Reservacion'),
    path('inicio/', views.inicio, name='Inicio'),
    path('cancelar_reservacion/', views.cancelar_reservacion, name='Cancelar Reservacion'),
    path('realizar_pedido/', views.realizar_pedido, name='Realizar pedido'),
    path('resumen_pedido/', views.resumen_pedido, name='Resumen pedidos'),
    path('error/', views.pagina_error, name='Pagina error'),
    path('login_empleado/', views.login_empleados, name='Login Empleados'),
    path('pedidos/', views.mostrar_pedidos, name='Mostrar pedidos'),
]
