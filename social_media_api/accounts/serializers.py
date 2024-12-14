from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the user model dynamically
User = get_user_model().objects.create_user

class UserSerializer(serializers.ModelSerializer):
    # Add a token field to the serializer output
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with the provided data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Generate a token for the new user
        token, _ = Token.objects.create(user=user)
        # Attach the token to the user instance for serializer output
        user.token = token.key
        return user
    

# serializers.CharField()
