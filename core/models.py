from django.db import models

# Create your models here.
class Site(models.Model):
    """Model representing a travel or vacation website."""
    site_name = models.CharField(max_length=200, default='N/A', help_text='Enter the name of a free to access programming book.')
    description = models.TextField(max_length=1000, default='N/A', help_text='Enter a description of the book.')
    date_added = models.DateTimeField(auto_now_add=True)
    uRL = models.TextField(max_length=1000, default='N/A', help_text='Enter the URL of the book.')

    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
