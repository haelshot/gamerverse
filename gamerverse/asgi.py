"""
WSGI config for gamerverse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.asgi import get_asgi_application
from ninja import NinjaAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamerverse.settings")

# application = get_wsgi_application()
django_asgi = get_asgi_application()
# from api import api as api_router

# # Create a Ninja API instance
# api = NinjaAPI()
# api.add_router('api', api_router)

# # Combine Django ASGI application and Ninja API
# def application(scope):
#     if scope['type'] == 'http':
#         return django_asgi(scope)
#     elif scope['type'] == 'websocket':
#         return api(scope)
