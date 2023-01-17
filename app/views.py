from .models import CustomUser
from rest_framework import viewsets
from .serializers import UserSerializer
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
