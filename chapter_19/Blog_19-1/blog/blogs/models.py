from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """Each blog posts content"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the model"""
        return self.title