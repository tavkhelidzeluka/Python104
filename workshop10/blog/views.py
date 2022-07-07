from django.shortcuts import render
from blog.models import Post

# Create your views here.
"""
Post Create View                    - render post form on page and create post object in database
Post Edit View                      - render post form (pre filled) and update post object in database
Post Delete View                    - render button to ask user if they're sure to 
                                    delete and after that delete post from db
Post List View (Home View)          - Where all posts are rendered with their recent 1-2 comments
Post Detail View                    - render all details about post with their comments
"""

def home_view(request):
    posts = Post.objects.all()

    return render(request, 'home.html', context={
        'posts': posts
    })


def post_detail_view(request, pk: int):
    post = Post.objects.get(pk=pk)

    return render(request, 'post_details.html', {
        'post': post
    })


