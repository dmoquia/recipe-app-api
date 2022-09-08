"""
Views for the user API
"""

from rest_framework import generics
# from here
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# to here
from user.serializers import (
    UserSerializer,
    # from here
    AuthTokenSerializer,
    # to here
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
# from here

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES