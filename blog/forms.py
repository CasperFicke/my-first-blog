from django import forms
from .models import Post, Comment

# Toelichting invoegen
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#toelicting invoegen
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)