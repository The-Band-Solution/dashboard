from .base import *
from decouple import config
import dj_database_url

DEBUG = True

SECRET_KEY = config('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE_TEST'),
        'NAME': config('DB_NAME_TEST'),
        'USER': config('DB_USER_TEST'),
        'PASSWORD': config('DB_PASSWORD_TEST'),
        'HOST': config('DB_HOST_TEST'),
        'PORT': config('DB_PORT_TEST'),
    }
}
