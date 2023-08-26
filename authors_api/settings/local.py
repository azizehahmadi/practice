from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default='django-insecure-yl26v(t2w(ok2g0ev*%5je^!%n=h(x4f1*th@wwt-k435sgzbu')

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']