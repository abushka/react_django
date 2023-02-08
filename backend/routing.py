from django.urls import path
from app import consumers

websocket_urlpatterns = [
    path("chats/<conversation_name>/", consumers.ChatConsumer.as_asgi()),
    path("notifications/", consumers.NotificationConsumer.as_asgi()),
    ]