from pyexpat import model
from django.db import models

class Pqrs_person(models.Model):
    type_document=  models.CharField(max_length=30)             #opciones
    identification_number=models.IntegerField()                 #parentesis
    name=           models.CharField(max_length=30)
    last_name=      models.CharField(max_length=30)
    num_cell=       models.IntegerField(null=True, blank=True)  #verificacion
    num_house=      models.IntegerField(null=True, blank=True)  #verificacion
    email=          models.EmailField()                         #parentesis
    created=        models.DateField(auto_now_add=True)


class Pqrs_tiket(models.Model):
    author=         models.ForeignKey(Pqrs_person,on_delete=models.CASCADE) # explicar
    ticket_title=   models.CharField(max_length=30)
    ticket_type=    models.CharField(max_length=30)
    ticket_content= models.CharField(max_length=250)
    state=          models.BooleanField(default=False)                      # como se maneja
    created=        models.DateField(auto_now_add=True)


