from tabnanny import verbose
from django.db import models

TICKET_TYPE_CHOICES=[
        ('P','pregunta' ),
        ('Q','queja' ),
        ('R','reclamo'),
        ('S','sugerencias')
    ]

TYPE_DOCUMENT_CHOICES=[
        ('CC','cedula de ciudadania' ),
        ('TI','tarjeta de identidad' ),
        ('CE','cedula de extranjeria'),
    ]

class Pqrs(models.Model):

    type_document=  models.CharField(max_length=30, choices= TYPE_DOCUMENT_CHOICES, default= 'CC')
    identification_number=models.IntegerField()      
    name=           models.CharField(max_length=30)
    last_name=      models.CharField(max_length=30)
    num_cell=       models.PositiveBigIntegerField(null=True, blank=True)  #verificacion
    num_house=      models.PositiveBigIntegerField(null=True, blank=True)  #verificacion
    email=          models.EmailField(max_length=50)
    ticket_title=   models.CharField(max_length=30)
    ticket_type=    models.CharField(max_length=30, choices= TICKET_TYPE_CHOICES, default='P')
    ticket_content= models.TextField(max_length=250)
    state=          models.BooleanField(default=False)
    created=        models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='pqrs'
        verbose_name_plural='pqrss'
        ordering=['id']


