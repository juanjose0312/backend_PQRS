MYSQL = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'HOST':     'localhost',
        'NAME':     '',
        'USER':     'root',
        'PASSWORD': '',
        'PORT':     '3306',
        'OPTION':   {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}