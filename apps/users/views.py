from rest_framework import viewsets

from apps.users.serializers import UserSerializer
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


