# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )

#SITE_ID = 3 # this depends on http://127.0.0.1:8000/en/admin/sites/site/
# we started with example.com in there, I deleted that so our first site is actually no. 2
