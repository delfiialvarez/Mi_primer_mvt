from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import familiares

def crear_familiares(request):
    familiar_creado = familiares.objects.create(nombre= "Violeta", apellido= "Fernandez", edad=45, estado_civil=False)
    print(familiar_creado)
    return HttpResponse ("Familiar agregado")

def lista_familiares(request):
    todos_los_familiares = familiares.objects.all()
    context = {
        "familiar": todos_los_familiares,
    }
    return render(request,"lista_de_familiares.html", context=context) 