from rest_framework import serializers #to see api in browser
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='detail', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'user', 'title', 'content', 'image']#create fields that will be in api


# class PostCreateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Post
#         fields = ['user', 'title', 'content', 'image']
