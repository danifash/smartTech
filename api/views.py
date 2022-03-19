from rest_framework import viewsets
from django.contrib.auth import get_user_model
from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UsersSerializer
    filterset_fields = ['username', 'first_name']


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_fields = ['author']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = models.Rate
    serializer_class = serializers.RateSerializer
