from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.views import ConversationViewSet, MessageViewSet
from app.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r'conversations', ConversationViewSet, basename='ConversationViewSet')
router.register(r'users', UserViewSet, basename='UserViewSet')
router.register(r'messages', MessageViewSet, basename='messages')


app_name = "api"
urlpatterns = router.urls