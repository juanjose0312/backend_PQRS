from tabnanny import verbose
from django.db import models

class Pqrs_person(models.Model):

    TYPE_DOCUMENT_CHOICES=[
        ('CC','cedula de ciudadania' ),
        ('TI','tarjeta de identidad' ),
        ('CE','cedula de extranjeria'),
    ]
    type_document=  models.CharField(max_length=30, choices= TYPE_DOCUMENT_CHOICES, default= 'CC')
    identification_number=models.IntegerField(unique=True)      
    name=           models.CharField(max_length=30)
    last_name=      models.CharField(max_length=30)
    num_cell=       models.PositiveBigIntegerField(null=True, blank=True)  #verificacion
    num_house=      models.PositiveBigIntegerField(null=True, blank=True)  #verificacion
    email=          models.EmailField(max_length=50)                                     #parentesis

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='users'
        verbose_name='user'
        verbose_name_plural='users'
        ordering=['id']


class Pqrs_tiket(models.Model):

    TICKET_TYPE_CHOICES=[
        ('P','pregunta' ),
        ('Q','queja' ),
        ('R','reclamo'),
        ('S','sugerencias')
    ]
    author=         models.ForeignKey(Pqrs_person,on_delete=models.CASCADE) # explicar
    ticket_title=   models.CharField(max_length=30)
    ticket_type=    models.CharField(max_length=30, choices= TICKET_TYPE_CHOICES, default='p')
    ticket_content= models.TextField(max_length=250)
    state=          models.BooleanField(default=False)                      # como se maneja
    created=        models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ticket_title
    
    class Meta:
        db_table='tikes'
        verbose_name='tiket'
        verbose_name_plural='tikets'
        ordering=['id']


