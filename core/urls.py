from django.urls import path
from . import views
from django.db import models
from django.urls import reverse
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('comments/<int:post_id>/', views.comments, name='comments'),

    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),
    path('destinations/', views.DestinationListView.as_view(), name='destinations'),

]