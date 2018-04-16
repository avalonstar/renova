from configurations import values

from .base import Base as Settings


class Development(Settings):
    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(True)

    CORS_ORIGIN_REGEX_WHITELIST = (
        r'^(https?://)?localhost',
        r'^(https?://)?127.',
    )
