from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

class SnippetListView(generics.ListCreateAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


