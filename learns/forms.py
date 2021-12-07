from django import forms

from learns.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author']
