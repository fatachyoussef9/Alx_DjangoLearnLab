from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import user_feed
from . import views


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
    path('posts/<int:pk>/like/', views.like_post),
    path('posts/<int:pk>/unlike/', views.unlike_post),
]