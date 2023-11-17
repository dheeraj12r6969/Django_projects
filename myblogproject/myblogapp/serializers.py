from rest_framework import serializers
from .models import Post, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'publication_date', 'updated_at')
