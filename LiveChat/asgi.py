"""
ASGI config for LiveChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import wsPattern
from channels.auth import AuthMiddlewareStack
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LiveChat.settings')

http_response_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": http_response_app,
    "websocket": URLRouter(wsPattern),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.wsPattern
        )
    )
})
