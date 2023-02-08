from django.contrib import admin
from .models import CustomUser, Conversation, Message

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Conversation)
admin.site.register(Message)
