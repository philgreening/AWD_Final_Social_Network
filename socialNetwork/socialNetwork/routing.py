from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import socialApp.routing

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(socialApp.routing.websocket_urlpatterns))

})