from django.urls import path

from posts.models import Post
from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='post_list'),
]
