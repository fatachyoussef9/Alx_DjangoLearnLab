from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from .serializers import PostSerializer, CommentSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#  Post.objects.filter(author__in=following_users).order_bys



@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        # Create a notification for the post author
        content_type = ContentType.objects.get_for_model(Post)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target_content_type=content_type,
            target_object_id=post.id
        )
        return Response({"message": "Post liked"})
    return Response({"message": "You already liked this post"}, status=400)

@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(id=pk)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
        return Response({"message": "Post unliked"})
    return Response({"message": "You haven't liked this post yet"}, status=400)