from django.shortcuts import render, HttpResponse
import random
from reservaciones.models import Reservacion, Cliente, ItemMenu, Pedido

def home(request):

    return render(request, 'reservaciones/home.html')

def login_empleados(request):

    return render(request, 'reservaciones/login_empleados.html')

def inicio(request):
    reservaciones = Reservacion.objects.filter(estado_reservacion='pendiente')
    pedidos = Pedido.objects.all()
    return render(request, 'reservaciones/inicio.html',{'reservaciones':reservaciones, 'pedidos':pedidos})

def crear_reservacion(request):
    mensaje = ''
    if request.POST:
        fecha = request.POST['fecha_reserva']
        hora = request.POST['hora_reserva']
        numero_personas = request.POST['numero_personas']
        cliente = Cliente.objects.get(id='1')

        codigo_reservacion = str (random.randint(1000, 9999))

        if (Reservacion.objects.filter(fecha= fecha) and Reservacion.objects.filter(hora= hora)):
            mensaje = 'ERROR: la fecha y hora escogida ya esta reservada. Escoja una fecha o hora diferente.'
            return render(request, 'reservaciones/crear_reservacion.html', {'mensaje_resultado':mensaje})
        else:
            op = Reservacion(numero_personas=numero_personas, codigo_reserva=codigo_reservacion, fecha=fecha, hora=hora, numero_identidad_cliente=cliente, estado_reservacion='pendiente')
            op.save()
            mensaje = 'RESERVA EXITOSA: su reserva fue registrada para el dia %s a las %s horas' %(fecha, hora)
            return render(request, 'reservaciones/crear_reservacion.html', {'mensaje_resultado':mensaje})
    return render(request, 'reservaciones/crear_reservacion.html', {'mensaje_resultado':mensaje})

def cancelar_reservacion(request):
    mensaje = ''
    if request.POST:
        codigo = request.POST['codigo_cancelar']
        if(Reservacion.objects.filter(codigo_reserva=codigo)):
            reservacion = Reservacion.objects.get(codigo_reserva=codigo)
            if (reservacion.estado_reservacion != 'cancelado' and reservacion.estado_reservacion != 'realizada'):
                reservacion.estado_reservacion = 'cancelado'
                reservacion.save()
                mensaje = 'CANCELACION EXITOSA: la reservacion con codigo %s a sido cancelada' %(codigo)
                return render(request, 'reservaciones/cancelar_reservacion.html', {'mensaje_resultado': mensaje})
            else:
                mensaje = 'ERROR: la reservacion con codigo %s ya fue cancelada o se llevo acabo' %(codigo)
                return render(request, 'reservaciones/cancelar_reservacion.html', {'mensaje_resultado': mensaje})
        else:
            mensaje = 'ERROR: la reservacion con codigo %s no se encuentra pendiente o el codigo no es valido' %(codigo)
            return render(request, 'reservaciones/cancelar_reservacion.html', {'mensaje_resultado': mensaje})
    return render(request, 'reservaciones/cancelar_reservacion.html', {'mensaje_resultado': mensaje})

def realizar_pedido(request):
    codigo = request.POST['codigo_inicio']
    if request.POST:
        if(Reservacion.objects.filter(codigo_reserva=codigo)):
            reservacion = Reservacion.objects.get(codigo_reserva=codigo)
            if (reservacion.estado_reservacion != 'cancelado' and reservacion.estado_reservacion != 'realizada'):
                return render(request, 'reservaciones/realizar_pedido.html')
            else:
                reservacion = Reservacion.objects.filter(estado_reservacion='pendiente')
                return render(request, 'reservaciones/inicio.html', {'reservaciones':reservacion})
        else:
            reservacion = Reservacion.objects.filter(estado_reservacion='pendiente')
            return render(request, 'reservaciones/inicio.html', {'reservaciones':reservacion})
    return render(request, 'reservaciones/realizar_pedido.html')

def resumen_pedido(request):
    platos, total_cuenta= [], 0
    for i in range(1, 10):
        try:
            entrante = request.POST['entrante'+ str (i)]
            platos.append(entrante)
        except KeyError:
            print('')
    for i in range (1, 10):
        try:
            fuerte = request.POST['fuerte'+ str (i)]
            platos.append(fuerte)
        except KeyError:
            print('')
    for i in range (1, 10):
        try:
            postre = request.POST['postre'+ str (i)]
            platos.append(postre)
        except KeyError:
            print('')
    metodo_pago = request.POST['metodo_pago']

    numero_pedido = str(random.randint(10000, 99999))
    for plato in platos:
        item = ItemMenu.objects.get(codigo_item=plato)
        pedido = Pedido(numero_pedido=numero_pedido, codigo_item=item, valor=item.valor, estado_pedido='Cocinando')
        pedido.save()
        total_cuenta += item.valor

    return render(request, 'reservaciones/resumen_pedido.html',{'metodo_pago':metodo_pago, 'total_cuenta':total_cuenta, 'numero_pedido':numero_pedido})

def pagina_error(request):

    return render(request, 'reservaciones/pagina_error.html')

def mostrar_pedidos(request):

    return render(request, 'reservaciones/mostrar_pedidos.html')

