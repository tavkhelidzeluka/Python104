from django.db import models


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
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    
