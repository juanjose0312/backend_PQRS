from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from django.views import View
from .models import Pqrs
import json

class Pqrs_view (View):

    @method_decorator(csrf_exempt)                          # metodo que ignora los parametros de seguridad CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,id=0):                                     # funcion de get 
        if(id>0):                                                   # filtra si la peticion de id busca a una en especifica o a todas 
            pqrss=list(Pqrs.objects.filter(id=id).values())         # consulta, filtra por id y lo convierte en una lista
            if len(pqrss)>0:                                        # si hay listas agregadas las muesta 
                pqrs=pqrss[0]                                      
                datos={'message':'Success','Pqrs': pqrs}
            else :                                                  # de lo contrario informa que no encontro listas
                datos={'message':'pqrs not found...'}
            return JsonResponse(datos)                              # devuelve la informacion como .Jason
        else:
            pqrss=list(Pqrs.objects.values())                       # consulta y lo convierte en una lista
            if len(pqrss)>0:                                    
                datos={'message':'Success','Pqrs': pqrss}
            else :                                              
                datos={'message':'pqrs not found...'}
            return JsonResponse(datos)                          


    def post(self,request):                                 # funcion de post
        jd=json.loads(request.body)                         # convierte el .Json a una lista
        Pqrs.objects.create(                                # citando la lista del .Json crea un nuevo item en la db
            type_document=        jd['type_document'],
            identification_number=jd['identification_number'],
            name=       jd['name'],
            last_name=  jd['last_name'],
            num_cell=   jd['num_cell'],
            num_house=  jd['num_house'],
            email=      jd['email'],
            ticket_title=   jd['ticket_title'],
            ticket_type=    jd['ticket_type'],
            ticket_content= jd['ticket_content'],
            state=          jd['state'],
            created=        jd['created'],
        )
        datos={'message':'Success'}                         # envia un mensaje de exito
        return JsonResponse(datos)


    def put(self,request,id):
        pass


    def delete(self,request,id):                            # funcion post
        pqrss=list(Pqrs.objects.filter(id=id).values())     # consulta, filtra por id y lo convierte en una lista
        if len(pqrss)>0:                                    # evalua si existe o esta vacion 
            Pqrs.objects.filter(id=id).delete()             # elimina 
            datos={'message':'Success'}
        else:
            datos={'message':'pqrs not found...'}
        return JsonResponse(datos)

class option(View):

    @method_decorator(csrf_exempt)                          # metodo que ignora los parametros de seguridad CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,id=0):

        if(id==1):
            type_document=[
                ('CC','cedula de ciudadania' ),
                ('TI','tarjeta de identidad' ),
                ('CE','cedula de extranjeria'),
            ]
            datos={'message':'Success','type_document': type_document}
            return JsonResponse(datos)

        elif(id==2):                                             
            type_ticket=[
                ('P','pregunta' ),
                ('Q','queja' ),
                ('R','reclamo'),
                ('S','sugerencias')
            ]
            datos={'message':'Success','type_ticket': type_ticket}
            return JsonResponse(datos)
        
        else:                                              
            datos={'message':'pqrs not found...'}
            return JsonResponse(datos) 

    
