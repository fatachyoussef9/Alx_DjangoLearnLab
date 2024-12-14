from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def follow_user(request, user_id):
#     try:
#         user_to_follow = CustomUser.objects.get(id=user_id)
#         if user_to_follow != request.user:
#             request.user.following.add(user_to_follow)
#             return Response({'message': 'You are now following this user.'}, status=status.HTTP_200_OK)
#         return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
#     except CustomUser.DoesNotExist:
#         return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def unfollow_user(request, user_id):
#     try:
#         user_to_unfollow = CustomUser.objects.get(id=user_id)
#         if user_to_unfollow in request.user.following.all():
#             request.user.following.remove(user_to_unfollow)
#             return Response({'message': 'You have unfollowed this user.'}, status=status.HTTP_200_OK)
#         return Response({'error': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
#     except CustomUser.DoesNotExist:
#         return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """
    Allows the authenticated user to follow another user.
    """
    try:
        user_to_follow = CustomUser.objects.get(pk=user_id)
        if user_to_follow == request.user:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """
    Allows the authenticated user to unfollow another user.
    """
    try:
        user_to_unfollow = CustomUser.objects.get(pk=user_id)
        if user_to_unfollow in request.user.following.all():
            request.user.following.remove(user_to_unfollow)
            return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)

        return Response({'error': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
