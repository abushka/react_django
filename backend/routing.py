from django.urls import path
from app import consumers

websocket_urlpatterns = [path("", consumers.ChatConsumer.as_asgi())]