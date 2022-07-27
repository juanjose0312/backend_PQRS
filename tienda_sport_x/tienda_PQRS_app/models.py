from django.core.validators import RegexValidator
from tabnanny import verbose
from django.db import models



class Pqrs(models.Model):

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

    type_document=  models.CharField(max_length=30, choices= TYPE_DOCUMENT_CHOICES, default= 'CC')
    identification_number=models.IntegerField()      
    name=           models.CharField(max_length=30)
    last_name=      models.CharField(max_length=30)
    num_cell_Regex = RegexValidator(regex = r"^\+?1?\d{10,13}$")
    num_cell =     models.CharField(validators = [num_cell_Regex], max_length = 16, null=True, blank=True)
    num_house_Regex = RegexValidator(regex = r"^\+?1?\d{7,10}$")
    num_house =     models.CharField(validators = [num_house_Regex], max_length = 16, null=True, blank=True)
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



