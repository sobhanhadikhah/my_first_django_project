from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title","content"]
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def validate(self, attrs):
        # Check if both passwords match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        # Remove the password confirmation field from validated data
        validated_data.pop('password2')
        # Create the user with the provided data
        user = User.objects.create_user(**validated_data)
        return user