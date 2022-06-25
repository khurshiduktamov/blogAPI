from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly
from .models import Post

# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class PostListAPIView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class UserListAPIView(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer