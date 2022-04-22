from rest_framework import serializers #to see api in browser
from rest_framework.reverse import reverse

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='detail', read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'user', 'title', 'content', 'image']#create fields that will be in api

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("detail", kwargs={'id': obj.id}, request=request)


