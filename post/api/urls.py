from django.urls import path
from .views import PostListAPIView, PostCreateAPIView, PostDetailAPIView


urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:id>/', PostDetailAPIView.as_view(), name='detail'),
]