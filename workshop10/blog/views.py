import django
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Post, Rating
from django.http import HttpResponseBadRequest
from django.views.generic import CreateView

from blog.forms import PostForm


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
    post_create_form = PostForm()

    return render(request, 'home.html', context={
        'posts': posts,
        'form': post_create_form
    })


def post_create_view(request):
    if request.method == 'GET':
        return redirect('blog:home')

    form = PostForm(request.POST, request.FILES)

    if not form.is_valid():
        return redirect('blog:home')

    form.save(user=request.user)
    return redirect('blog:home')


def post_detail_view(request, pk: int):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post_details.html', {
        'post': post
    })


@login_required
def post_rate_view(request, pk: int):
    # print(request.GET)
    # if not request.user.is_authenticated:
    #     pass

    if request.method == 'GET':
        # User tried to like with get request
        return redirect('blog:home')

    try:
        is_positive = bool(int(request.POST['is_positive']))
    except ValueError:
        # User tried to send invalid data
        return redirect('blog:home')

    
    post = get_object_or_404(Post, pk=pk)
    try:
        rating, created = Rating.objects.get_or_create(post=post, user=request.user, is_positive=is_positive)
        if not created:
            # user already has liked this post
            return redirect('blog:home')
    except django.db.utils.IntegrityError:
        rating = Rating.objects.get(post=post, user=request.user)
        rating.is_positive = not rating.is_positive
        rating.save()

    return redirect('blog:home')




