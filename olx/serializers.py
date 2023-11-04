from rest_framework import serializers
from olx import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "title"
        )


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.SubCategory
        fields = (
            "id",
            "title",
            "category",
            "is_popular"
        )


class PostSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()

    class Meta:
        model = models.Post
        fields = (
            "id",
            "title",
            "content",
            "image",
            "price",
            "is_vip",
            "subcategories",
            "location",
            "phone",
            "created_at",
            "updated_at",
            "views",
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "id",
            "title",
            "created_at",
        )