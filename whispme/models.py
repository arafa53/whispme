from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=14)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'message by ' + self.name

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='images/')
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=25)
    slug = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    def __str__(self):
        return 'Post by ' + self.author

class PostComment(models.Model):
    sno =models.AutoField(primary_key=True)
    comment =models.TextField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp =models.DateTimeField(default=now)
    def __str__(self):
        return 'Post by ' + self.user.username


class Image(models.Model):
    caption=models.CharField(max_length=100)
    image = models.ImageField(upload_to='myphoto/')
    content = models.TextField()
    def __str__(self):
        return 'Post by ' + self.caption
    
    
    

