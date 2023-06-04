from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
class Category (models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name



class Post (models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    tags = TaggableManager()
    img = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(timezone.now)
    description = models.TextField(max_length=1500)
    category = models.ForeignKey(Category, related_name='post_category',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
            super().save(*args,**kwargs)
