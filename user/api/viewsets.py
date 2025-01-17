from rest_framework import viewsets
from user.api import serializers
from user import models

class UserViewset(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
