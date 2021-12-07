from django import forms

# import GeeksModel from models.py
from .models import Post

# create a ModelForm
class PostForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Post
        exclude = ('upvote', 'downvote')
        fields = "__all__"