from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    is_popular = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    
    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.title


class User(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images")

    is_popular = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    price = models.PositiveIntegerField()
    views = models.PositiveIntegerField(default=0)

    status = (
        ('New', 'new'),
        ('Ishlatilgan', 'ishlatilgan'),
    )
    status = models.CharField(max_length=255, choices=status, default='new')

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    