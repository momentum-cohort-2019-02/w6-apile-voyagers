from django.urls import path
from . import views
from django.db import models
from django.urls import reverse
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),

    path('posts/', views.PostListView.as_view(), name='posts'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),

    # url('register/$',views.register, name='register'),rvr
]