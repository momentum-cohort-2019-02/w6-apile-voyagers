from django.shortcuts import render
from core.models import Post, Comment, Destinations
from core.forms import CommentForm
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from core.forms import CommentForm
from django.http import Http404
from django.contrib import messages
from django.views.decorators.http import require_http_methods

# Create your views here.


def index(request):
    """View function for home page of site."""
    posts = Post.objects.all()
    # Render the HTML template index.html with the data in the context variable
    response = render(request, 'index.html', {
        "posts": posts,
    })
    return response

def comments(request, post_id):
    """View function for home page of site."""
    comments = Comment.objects.filter(post__id=post_id)
    post = Post.objects.get(id=post_id)
    form = CommentForm()
    # Render the HTML template index.html with the data in the context variable
    response = render(request, 'core/comment.html', {
        "comments": comments,
        "post_id": post_id,
        "post": post,
        "comment_form": form
    })
    return response  
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



class PostListView(generic.ListView):
    model = Post
    paginate_by = 3

class DestinationListView(generic.ListView):
    model = Destinations

@require_http_methods(['POST'])
# @login_required
def new_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if post is None:
        raise Http404('No task matches the given query.')

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.commenter = post.author #TODO: post.author should be replaced with the logged in user
        comment.save()
    else:
        messages.error(request, 'We had a problem saving your comment.')
    return redirect('comments',post_id=post_id)
