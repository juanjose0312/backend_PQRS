# juan_jose-sport_x_inlazz
introduccion 

esta es un app encargada de maneja el CRUD en una base de datos
que fue modelada para recibir informacion PQRs 

como hacer uso ?

para utilizar las api rest ingrese al link:

- para agregar : 
    http://127.0.0.1:8000/api/pqrs/ # en el body introduce con este esquema
    {
        "type_document":    "",         (type:string, max length=30)
        "identification_number": ,      (type:Integer,max num = 2147483647)
        "name":             "",         (type:string, max length=30)    
        "last_name":        "",         (type:string, max length=30)
        "num_cell":           ,         (type:PositiveBigInteger, max num =9223372036854775807)
        "num_house":          ,         (type:PositiveBigInteger, max num =9223372036854775807)
        "email":            "",         (type:email , max length=50)
        "ticket_title":     "",         (type:string, max length=30)
        "ticket_type":      "",         (type:string, max length=30)
        "ticket_content":   "",         (type:string, max length=250)   
        "state":         false,         (type:boolean)
    }

- para listar :
    http://127.0.0.1:8000/api/pqrs/

- para selecionar :
    http://127.0.0.1:8000/api/pqrs/ #al final agrega el numero de id que desea listar

- para borrar :
    http://127.0.0.1:8000/api/pqrs/ #al final agrega el numero de id que desea eliminar

- para revisar las opciones de tipos de documento :

    TYPE_DOCUMENT_CHOICES=[
            ('CC','cedula de ciudadania' ),
            ('TI','tarjeta de identidad' ),
            ('CE','cedula de extranjeria'),
        ]

- para revisar las opciones de tipos de PQRS  :

    TICKET_TYPE_CHOICES=[
            ('P','pregunta' ),
            ('Q','queja' ),
            ('R','reclamo'),
            ('S','sugerencias')
        ]

- para ingresar a la pagina del admin :
    http://127.0.0.1:8000/admin/
    super usuario
        user :      juan
        password:   inlazz2022
