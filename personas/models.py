from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais= models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'
    
class Persona(models.Model):
    nombre =  models.CharField(max_length=255)
    apellido =models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #con CASCADE se eliminaria el registro si se elimina el registro padre deomicilio el de persona tmbn
    domicilio=models.ForeignKey(Domicilio, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        #Se mostrara en el modulo de personas del admin
        #String format
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'

