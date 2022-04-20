from rest_framework import serializers #to see api in browser
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['user', 'title', 'content']#create fields that will be in api


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['user', 'title', 'content']
