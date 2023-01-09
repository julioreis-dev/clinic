from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = 'django-insecure-u_r5=ao@=$g0ulnyhn423c%!y25pce0@f5gcvhv#!fj!g9w5o3'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG_DEV')
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
