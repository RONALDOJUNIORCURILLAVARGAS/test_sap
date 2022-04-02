
from django.forms import EmailInput, ModelForm,TextInput
from personas.models import Persona,Domicilio

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        #Indicamos que usaremos todo los atributos
        fields ='__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }
class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        #Indicamos que usaremos todo los atributos
        fields ='__all__'
        widgets = {
            'no_calle':TextInput(attrs={'type':'number'})
        }