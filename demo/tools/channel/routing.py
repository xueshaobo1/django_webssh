#from django.urls import path
from django.conf.urls import url
from demo.tools.channel import websocket

websocket_urlpatterns = [
    url('webssh/', websocket.WebSSH),
]
