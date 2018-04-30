from channels.auth import AuthMiddlewareStack
from channels.security.websocket import OriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
import game.routing

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket':
        OriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    game.routing.websocket_urlpatterns
                )
            ),
            ['*']
        ),
})
