from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona

# Create your views here.
def bienvenido(request):

    no_personas=Persona.objects.count()
    #personas=Persona.objects.all()

    #Prdenar de manera ascendente
    personas=Persona.objects.order_by('id')
    #Ordenar de manera descendente
    #personas=Persona.objects.order_by('-id')



    #creanis un diccionario para mandar al html
    #mensajes={'msg1':'Valor mensaje 1','msg2':'Valor 2'}
    #return render(request,'bienvenido.html',mensajes)
    return render(request,'bienvenido.html',{'no_personas':no_personas, 'personas':personas})
