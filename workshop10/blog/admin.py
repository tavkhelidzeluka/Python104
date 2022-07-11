from django.contrib import admin

from blog.models import Post, Rating, Comment


@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'author', 'create_date']
    readonly_fields = ['create_date', 'edit_date']


# Register your models here.
admin.site.register([Rating, Comment])
