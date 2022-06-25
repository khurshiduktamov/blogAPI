from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet
# from .views import PostDetailAPIView, PostListAPIView, UserListAPIView, UserDetailAPIView

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls



# urlpatterns = [
#     path('<int:pk>/', PostDetailAPIView.as_view()),
#     path('', PostListAPIView.as_view()),
#     path('users/', UserListAPIView.as_view()),
#     path('users/<int:pk>/', UserDetailAPIView.as_view()),
# ]