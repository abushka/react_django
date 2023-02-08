from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from .serializers import MessageSerializer
import json
from uuid import UUID
from .models import CustomUser, Conversation, Message


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class ChatConsumer(JsonWebsocketConsumer):
    """
    This consumer is used to show user's online status,
    and send notifications.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.user = None



    def connect(self):
        
        self.user = self.scope["user"]
        if not self.user.is_authenticated:
            return

        self.accept()
        self.conversation_name = f"{self.scope['url_route']['kwargs']['conversation_name']}"
        self.conversation, created = Conversation.objects.get_or_create(name=self.conversation_name)

        async_to_sync(self.channel_layer.group_add)(
            self.conversation_name,
            self.channel_name,
        )

        self.send_json(
            {
                "type": "online_user_list",
                "users": [user.username for user in self.conversation.online.all()],
            }
        )

        async_to_sync(self.channel_layer.group_send)(
            self.conversation_name,
            {
                "type": "user_join",
                "user": self.user.username,
            },
        )

        self.conversation.online.add(self.user)

        messages = self.conversation.messages.all().order_by("-timestamp")[0:10]
        message_count = self.conversation.messages.all().count()
        self.send_json(
            {
                "type": "last_50_messages",
                "messages": MessageSerializer(messages, many=True).data,
                "has_more": message_count > 5,
            }
        )

    def disconnect(self, code):
        if self.user.is_authenticated:
            # send the leave event to the room
            async_to_sync(self.channel_layer.group_send)(
                self.conversation_name,
                {
                    "type": "user_leave",
                    "user": self.user.username,
                },
            )
            self.conversation.online.remove(self.user)
        return super().disconnect(code)
        

    def get_receiver(self):
        usernames = self.conversation_name.split("__")
        for username in usernames:
            if username != self.user.username:
                # This is the receiver
                try:
                    get_custom_user = CustomUser.objects.get(username=username)
                except CustomUser.DoesNotExist:
                    get_custom_user = None
                return get_custom_user

    def receive_json(self, content, **kwargs):
        message_type = content["type"]

        if message_type == "chat_message":
            message = Message.objects.create(
                from_user=self.user,
                to_user=self.get_receiver(),
                content=content["message"],
                conversation=self.conversation,
            )

            async_to_sync(self.channel_layer.group_send)(
                self.conversation_name,
                {
                    "type": "chat_message_echo",
                    "name": self.user.username,
                    "message": MessageSerializer(message).data,
                },
            )
        return super().receive_json(content, **kwargs)
    



    def chat_message_echo(self, event):
        print(event)
        self.send_json(event)
    def chat_message_echo(self, event):
        print(event)
        self.send_json(event)

    @classmethod
    def encode_json(cls, content):
        return json.dumps(content, cls=UUIDEncoder)

    def user_join(self, event):
        self.send_json(event)