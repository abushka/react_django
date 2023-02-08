# myapi/urls.py
from django.urls import include, path
from .views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
