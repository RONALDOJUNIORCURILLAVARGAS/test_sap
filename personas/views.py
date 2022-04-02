

from django.shortcuts import get_object_or_404, redirect, render


from personas.models import Persona
from personas.forms import PersonaForm

#Se recibe el parametro que se envia en la variable id, puedes nombrarla como quieras
def detallePersonas(request,id):
    #persona=Persona.objects.get(pk=id)
    persona=get_object_or_404(Persona, pk=id)
    #se envia un objeto
    return render(request,'personas/detalle.html',{'persona':persona} )

#creamos el objeto de tipo persona
#Se debe incluir que se excluira del modelo, en este caso no se excluye nada
#PersonaForm = modelform_factory(Persona,exclude=[])

def nuevaPersona(request):
    #Evaluamos si enviamos o recibimos
    #el IF es Para enviar lo del formulario al modelo para hacer un insert
    #el ELSE es para capturar el objeto de PersonaForm y generar la tabla del formulario
    if request.method =='POST':
        formaPersona=PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else :
        formaPersona= PersonaForm()
    return render(request,'personas/nuevo.html',{'formaPersona':formaPersona}) 

def editarPersona(request,id):
    persona=get_object_or_404(Persona, pk=id)
    if request.method =='POST':
        formaPersona=PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else :
        #Cuando es de tipo GET recuperaremos el objeto a traves del ID
        formaPersona= PersonaForm(instance=persona)

    return render(request,'personas/editar.html',{'formaPersona':formaPersona}) 

def eliminarPersona(request,id):
    persona=get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')