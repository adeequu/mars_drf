from django.urls import path
from .views import PostListAPIView, PostCreateAPIView, PostDetailAPIView, PostUpdateAPIView, PostDestroyAPIView


urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:id>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', PostDestroyAPIView.as_view(), name='delete'),
]