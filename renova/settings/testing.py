from configurations import values

from .base import Base as Settings


class Testing(Settings):
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = DEBUG

    Settings.DATABASES['default']['NAME'] = 'test_renova'
    Settings.DATABASES['ragnarok'] = {
        'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'
    }
