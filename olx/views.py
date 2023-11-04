from rest_framework import generics
from olx.serializers import PostSerializer,CategorySerializer,SubCategorySerializer,UserSerializer
from olx.models import Post, User, Category, SubCategory


# Create your views here.
class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

