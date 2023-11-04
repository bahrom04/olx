from django.urls import path, include
from olx.views import PostViewSet, CategoryViewSet, SubCategoryViewSet, UserViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('categories/', CategoryViewSet.as_view()),
    path('subcategories/', SubCategoryViewSet.as_view()),
    path('users/', UserViewSet.as_view()),
    path('posts/', PostViewSet.as_view()),
    ]