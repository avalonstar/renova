from configurations import values

from .base import Base as Settings


class Development(Settings):
    DEBUG = values.BooleanValue(True)
