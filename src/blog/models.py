from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=200) #debería ser un resumen del body, podríamos coger solo las primeras lineas?
    body = models.TextField()
    image_url = models.URLField()
    postDate = models.DateTimeField(auto_now_add=True)
    #categories: heredadas de otra clase
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

