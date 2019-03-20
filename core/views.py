from django.shortcuts import render
from core.models import Post
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """View function for home page of site."""


    # num_posts = Post.objects.all().count()  


    # context = {
    #     'num_posts': num_posts,
        
    # }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html',)

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



# class PostListView(generic.ListView):
#     model = Site

# class PostDetailView(generic.DetailView):
#     model = Site
