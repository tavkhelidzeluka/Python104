import datetime
from distutils.command.upload import upload
from statistics import mode
from django.db import models

from users.models import User
from django.shortcuts import reverse


# Create your models here.
"""
Post Model
    - author            (User reference)
    - name              (string)
    - text              (string)
    / - image             (File) /

    - create date       (datetime)
    - edit date         (datetime)


Comment Model
    - author            (User reference)
    - post              (Post reference)
    - text              (string)

    - create date       (datetime)

Rating Model
    - user              (User reference)
    - post              (Post reference)
    - positive          (boolean)

"""

class Post(models.Model):
    # ORM - object relational mapper
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    text = models.TextField()

    create_date: datetime.datetime = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def get_create_date(self) -> str:
        return self.create_date.strftime('%d %b').upper()
    
    def get_likes(self) -> int:
        return self.rating_set.filter(is_positive=True).count()
    
    def get_dislikes(self) -> int:
        return self.rating_set.filter(is_positive=False).count()
    
    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})

    def rate_link(self):
        return reverse("blog:post-rate", kwargs={"pk": self.pk})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_positive = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'post')
