from django.db import models

# Create your models here.
class Post(models.Model):
    """Model representing a travel or vacation website."""
    site_name = models.CharField(max_length=200, default='N/A', help_text='Enter an article link to a vacation destination.')
    destination = models.CharField(max_length=200, default='N/A', help_text='Enter the destination')
    author = models.CharField(max_length=200, default='N/A', help_text='Enter the author of the article.')
    description = models.TextField(max_length=1000, default='N/A', help_text='Enter a description of the article.')
    date_added = models.DateTimeField(auto_now_add=True)
    uRL = models.TextField(max_length=1000, default='N/A', help_text='Enter the URL of the article.')

    
    def __str__(self):
        """String for representing the Model object."""
        return self.site_name

class Comment(models.Model):
    user_comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.user_comment
