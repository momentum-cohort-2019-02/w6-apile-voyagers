from django import forms
from core.models import Comment, Author

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    # password1 = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     #masks password text
    #     widget=forms.PasswordInput,
    # )

    class Meta:
        model = Author
        fields = ("username", "password", "name")

    
