from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=20, blank=True)
    blog = models.CharField(max_length=50, blank=True)
    blog_description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    def __str__(self):
        full_name = self.name+' '+self.password
        return self.full_name


