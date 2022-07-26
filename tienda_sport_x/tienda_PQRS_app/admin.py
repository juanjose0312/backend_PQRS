from django.contrib import admin
from tienda_PQRS_app.models import Pqrs_person,Pqrs_tiket

class person_admin(admin.ModelAdmin):
    readonly_fields=('created',)
    # permite visualisar en la pagina admin de una manera estetica
    list_display=   ('type_document','identification_number','name','last_name','num_cell','num_house','email','created')     
    list_filter=    ('identification_number','name')            # menu de filtros
    search_fields=  ('identification_number','name')            # opcion buscar
         
            

class tiket_admin(admin.ModelAdmin):
    readonly_fields=('created',)           
    list_display=('author','ticket_title','ticket_type','ticket_content','state','created')     
    list_filter=('state',)                        
    search_fields=('author',)

    

admin.site.register(Pqrs_person, person_admin)     
admin.site.register(Pqrs_tiket, tiket_admin) 
