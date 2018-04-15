from configurations import values

from .base import Base as Settings


class Development(Settings):
    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(True)

    CORS_ORIGIN_WHITELIST = (
        'localhost:3000',
        'localhost:3001',
    )
