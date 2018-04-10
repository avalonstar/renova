import os

from configurations import values

from .base import Base as Settings


class Testing(Settings):
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = DEBUG

    if 'TRAVIS' in os.environ:
        TRAVIS_ENVIRONMENT = True

    if TRAVIS_ENVIRONMENT:
        Settings.DATABASES['default'] = {
            'NAME': 'travisdb', 'USER': 'postgres', 'PASSWORD': '', 'PORT': ''
        }
    else:
        Settings.DATABASES['default']['NAME'] = 'test_renova'

    Settings.DATABASES['ragnarok'] = {
        'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'
    }
