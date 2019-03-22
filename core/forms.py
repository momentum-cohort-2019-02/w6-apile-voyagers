from django import forms
from core.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
    
