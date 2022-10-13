from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


class Blog(models.Model):
    CHOICES_WISHLIST = {
        ('liked', 'liked'),
        ('disliked', 'disliked'),
    }
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    choices_wishlist = models.CharField(max_length=10, choices=CHOICES_WISHLIST,null=True , blank=True)


    def __str__(self):
        return f'{self.user} - {self.title}'




class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='comments')
    text = models.TextField()
    data_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f' {self.user} -    user blog is : {self.blog}'

