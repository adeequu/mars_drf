from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework import permissions
from accounts.api.permissions import IsOwnerOrReadOnly


from post.api.serializers import PostSerializer
from post.models import Post
from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


class PostListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated] #is authenticatedorread only can read but cant update the data
    # authentication_classes = [SessionAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__incontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCreateAPIView(CreateAPIView): #write this to create post from api not from the admin
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin): #write mixin to see the button delete
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes = [SessionAuthentication] #with [] not the same -> #
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDestroyAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


