"""
WSGI config for renova project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'renova.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

application = get_wsgi_application()
