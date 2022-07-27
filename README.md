# juan_jose-sport_x_inlazz
## introduccion 

esta es un app encargada de maneja el CRUD en una base de datos <br>
que fue modelada para recibir informacion PQRs <br>

## como hacer uso ? <br>

### para utilizar las api rest ingrese al link: <br>

- **para agregar :** <br>
    [localhost:8000/api/pqrs/](localhost:8000/api/pqrs/) # en el body introduce con este esquema<br>
    {<br>
        "type_document":    "",         (type:string, max length=30)<br>   
        "identification_number":,       (type:Integer,max num = 2147483647)<br>
        "name":             "",         (type:string, max length=30)<br>  
        "last_name":        "",         (type:string, max length=30)<br>  
        "num_cell":           ,         (num : 10-13 digitos)<br>
        "num_house":          ,         (num : 7-11  digitos)<br>
        "email":            "",         (type:email , max length=50)<br>
        "ticket_title":     "",         (type:string, max length=30)<br>
        "ticket_type":      "",         (type:string, max length=30)<br>
        "ticket_content":   "",         (type:string, max length=250)<br>   
        "state":         false,         (type:boolean)<br>
    }<br>

- **para listar :**<br>
    [localhost:8000/api/pqrs/](localhost:8000/api/pqrs/)<br>

- **para selecionar :**<br>
    [localhost:8000/api/pqrs/](localhost:8000/api/pqrs/) #al final agrega el numero de id que desea listar<br>

- **para borrar :**<br>
    [localhost:8000/api/pqrs/](localhost:8000/api/pqrs/) #al final agrega el numero de id que desea eliminar<br>

- **para revisar las opciones de tipos de documento :**<br>
    [localhost:8000/api/option/1](localhost:8000/api/option/1)<br>

    TYPE_DOCUMENT_CHOICES=[<br>
            ('CC','cedula de ciudadania' ),<br>
            ('TI','tarjeta de identidad' ),<br>
            ('CE','cedula de extranjeria'),<br>
    ]<br>

- **para revisar las opciones de tipos de PQRS  :**<br>
    [localhost:8000/api/option/2](localhost:8000/api/option/2)<br>

    TICKET_TYPE_CHOICES=[<br>
            ('P','pregunta' ),<br>
            ('Q','queja' ),<br>
            ('R','reclamo'),<br>
            ('S','sugerencias')<br>
    ]<br>

- **para ingresar a la pagina del admin :**<br>
    [localhost:8000/admin/](localhost:8000/admin/)<br>
    super usuario<br>
        *user :*      juan<br>
        *password:*   inlazz2022<br>