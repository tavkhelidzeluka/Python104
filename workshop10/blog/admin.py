from django.contrib import admin

from blog.models import Post, Rating, Comment

# Register your models here.
admin.site.register([Post, Rating, Comment])
