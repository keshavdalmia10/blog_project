from django.shortcuts import render
from blog.models import Post
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import PostListSerializer,PostDetailSerializer,PostCreateSerializer,UserProfileSerializers
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .import models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from blog import permissions

# Create your views here.

class PostListAPIView(generics.ListAPIView):
    queryset=models.Post.objects.all()
    serializer_class=PostListSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset= models.Post.objects.all()
    serializer_class=PostDetailSerializer
    lookup_field='slug'

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset= models.Post.objects.all()
    serializer_class=PostDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnContent, IsAuthenticated)
    lookup_field='slug'

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset= models.Post.objects.all()
    serializer_class=PostDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnContent, IsAuthenticated)
    lookup_field='slug'
    
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class PostCreateAPIView(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnContent, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
    

class UserLoginApiView(ObtainAuthToken):
  """Handle creating user authentication tokens"""
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES 

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
    search_fields = ('name', 'email',)









        
        