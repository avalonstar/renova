import os

import dj_database_url

from configurations import values

from .base import Base as Settings


class Testing(Settings):
    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = DEBUG

    # Database Definition.
    # --------------------------------------------------------------------------
    if 'TRAVIS' in os.environ:
        TEST_DATABASE_URL = 'postgres://postgres@localhost/travisdb'
    else:
        TEST_DATABASE_URL = 'postgres://avalonstar@localhost:5432/test_renova'

    DATABASES = {
        'default': dj_database_url.parse(TEST_DATABASE_URL),
        'ragnarok': dj_database_url.parse('sqlite://:memory:')
    }
