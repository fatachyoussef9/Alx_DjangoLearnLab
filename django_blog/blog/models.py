from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager() 

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Tag name (e.g., "Django", "Python")
    slug = models.SlugField(unique=True)  # Slug for URL-friendly version of the name
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically create a slug from the name if it's not provided
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')
        super().save(*args, **kwargs)
