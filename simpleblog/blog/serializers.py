from rest_framework import serializers
from .import models

class UserProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=models.UserProfile
        fields = ('id', 'email', 'name','password')
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
        """Used to create a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class PostListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Post
        fields=('title','slug','content')

class PostDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Post
        fields=('id','title','slug','content')


class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Post
        fields=('title','content')



        

