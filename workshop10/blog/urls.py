from django.urls import path
from blog.views import home_view, post_detail_view, post_rate_view, post_create_view

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('posts/create/', post_create_view, name='post-create'),
    path('post/<int:pk>/', post_detail_view, name='post-detail'),
    path('post/<int:pk>/like/', post_rate_view, name='post-rate')
]
