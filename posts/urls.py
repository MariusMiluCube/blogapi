from os import name
from django.urls import path
from rest_framework.routers import SimpleRouter
from posts.models import Post
from .views import PostList, PostDetail, PostViewSet, UserList, UserDetail, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
