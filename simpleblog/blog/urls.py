from django.urls  import path,re_path,include
from django.contrib import admin
from blog import views
from .views import (
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    PostCreateAPIView,
    UserProfileViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)




urlpatterns = [
path('', include(router.urls)),
path('login/', views.UserLoginApiView.as_view()),
path('create/',PostCreateAPIView.as_view(), name='create'),
path('list/',PostListAPIView.as_view(), name='list'),
path('<slug>/',PostDetailAPIView.as_view(),name='detail'),
path('<slug>/edit/',PostUpdateAPIView.as_view(),name='update'),
path('<slug>/delete/',PostDeleteAPIView.as_view(),name='delete'),

    
]
    
