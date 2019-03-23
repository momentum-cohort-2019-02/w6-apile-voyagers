from django.db import models
from django.urls import reverse
# from slugger import AutoSlugField

# Create your models here.


class Author(models.Model):
    """Model representing user making a comment, create a post and vote"""
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Post(models.Model):
    """Model representing a travel or vacation website."""
    destination = models.CharField(max_length=200, default='N/A')
    site_name = models.CharField(max_length=200, default='N/A')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default='N/A')
    date_added = models.DateTimeField(auto_now_add=True)
    url = models.TextField(max_length=1000, default='N/A')
    # slug = AutoSlugField(unique=True, max_length=200, populate_from='site_name')

    
    def __str__(self):
        """String for representing the Model object."""
        return self.site_name

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
 
class Comment(models.Model):
    """Model representing user making a comment on a post"""
    comment = models.CharField(max_length=2000)
    commenter = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Vote(models.Model):
    """Model representing a user voting on a post"""
    voter = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.voter + self.post


class Destinations(models.Model):
    """Model representing destinations page."""
    destination = models.CharField(max_length=200, default='N/A')
    url = models.TextField(max_length=1000, default='N/A')
    site_name = models.CharField(max_length=200, default='N/A')

    def __str__(self):
        """String for representing the Model object."""
        return self.site_name


class Postlist(models.Model):
    """Model representing destinations page."""
    destination = models.CharField(max_length=200, default='N/A')
    url = models.TextField(max_length=1000, default='N/A')
    site_name = models.CharField(max_length=200, default='N/A')

    def __str__(self):
        """String for representing the Model object."""
        return self.site_name



