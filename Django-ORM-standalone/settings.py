DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
