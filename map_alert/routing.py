from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from alert import routing
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket':
        URLRouter(
            routing.websocket_urlpatterns
        )
})
