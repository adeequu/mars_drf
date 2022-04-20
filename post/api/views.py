from rest_framework.response import Response
from rest_framework.views import APIView


from post.api.serializers import PostSerializer
from post.models import Post
from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


# class PostAPIView(APIView): #get the list of all posts
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializers = PostSerializer(qs, many=True)
#         return Response(serializers.data) # the data will be appeared like json(dict) format


class PostListAPIView(ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__incontains=query)
        return qs


class PostCreateAPIView(CreateAPIView): #write this to create post from api not from the admin
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateAPIView(UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyAPIView(DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


