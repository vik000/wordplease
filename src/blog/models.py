from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    body = models.TextField()
    image_url = models.URLField()
    postDate = models.DateTimeField(auto_now_add=True)

