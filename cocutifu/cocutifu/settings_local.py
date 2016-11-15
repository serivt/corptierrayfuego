from .settings import *

DEBUG = True

# Debug secret key.
SECRET_KEY = 'nk_v#ka5-v0zm%7&ab6l8gy033zw(=5*b&&lvpvq=kd%8ofc!i'

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}