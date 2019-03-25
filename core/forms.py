from django import forms
from core.models import Comment, Post
from django.contrib.auth import (
    get_user_model,
    password_validation,
)

User = get_user_model()

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

class NewPostForm(forms.ModelForm):
    destination = forms.CharField(
        label='Destination',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'add a new destination'}))

    site_name = forms.CharField(
        label='website_name',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'add website'}))
   
    description = forms.CharField(
        label='Description',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'add description'}))
    
    url = forms.URLField(
        label='url',
        max_length=200,
       )
    
    class Meta:
        model = Post
        fields = ['destination', 'site_name', 'description', 'url'] 
    # def save(self, **kwargs):
    #     if self.is_valid():
    #         post_props  = {"description": self.cleaned_data['post']}
    #         post_props.update(kwargs)
    #         return Post.objects.create(**post_props)
    #     return None

