from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title[:50] 

    class Meta: 
        ordering = ["-updated","-created"]
