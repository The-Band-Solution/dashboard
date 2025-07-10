from .base import *
from decouple import config
import dj_database_url

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE_PRODUCTION'),
        'NAME': config('DB_NAME_PRODUCTION'),
        'USER': config('DB_USER_PRODUCTION'),
        'PASSWORD': config('DB_PASSWORD_PRODUCTION'),
        'HOST': config('DB_HOST_PRODUCTION'),
        'PORT': config('DB_PORT_PRODUCTION'),
    }
}