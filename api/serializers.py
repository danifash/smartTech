from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password', 'user_permissions', 'groups')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class PostDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostDescription
        fields = '__all__'


class PostImgUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostImgUrl
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    images = PostImgUrlSerializer()
    descriptions = PostDescriptionSerializer()

    class Meta:
        model = models.Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rate
        fields = '__all__'
