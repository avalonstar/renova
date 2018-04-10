from configurations import values

from .base import Base as Settings


class Production(Settings):
    DEBUG = values.BooleanValue(False)
