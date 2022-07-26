from django.contrib import admin
from tienda_PQRS_app.models import Pqrs

class person_admin(admin.ModelAdmin):
    readonly_fields=('created',)
    # permite visualisar en la pagina admin de una manera estetica
    list_display=   (
        'type_document','identification_number','name','last_name',
        'num_cell','num_house','email','ticket_title','ticket_type',
        'ticket_content','state','created')     
    list_filter=    ('identification_number','name','state')            # menu de filtros
    search_fields=  ('identification_number','name')                    # opcion buscar
    
admin.site.register(Pqrs, person_admin)     

