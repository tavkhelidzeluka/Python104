from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['name', 'text', 'image']
    
    def save(self, commit: bool = ..., user = None):
        post = super().save(commit=False)

        if commit:
            post.author = user
            post.save()
        return post

