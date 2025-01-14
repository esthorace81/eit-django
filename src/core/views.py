from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    año_actual = datetime.now().year
    context = {"año": año_actual}
    return render(request, "core/index.html", context)


def saludar(request):
    return HttpResponse("¡Hola Django!")


def saludar_con_etiqueta(request):
    return HttpResponse("<h1> Este es el título de mi App </h1>")


def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")


def tirar_dado(request):
    from random import randint

    tiro_dado = randint(1, 6)
    if tiro_dado == 6:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_dado} 🔥 Ganaste!"
    else:
        mensaje = f"Has tirado el 🎲 y has sacado {tiro_dado} 😉 Sigue intentando!"

    datos = {
        "titulo": "Tiro de datos",
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%H:%M:%S.%f"),
    }
    return render(request, "core/dados.html", context=datos)


def ejercicio_1(request):
    nombre = "Louis"
    apellido = "Van Beethoven"
    return render(request, "core/ejercicio_1.html", {"nombre": nombre, "apellido": apellido})


def ver_notas(request):
    lista_notas = [10, 8, 3, 7, 4, 5, 8]
    return render(request, "core/notas.html", {"notas": lista_notas})
