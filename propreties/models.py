from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.utils.text import slugify

class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    def __str__(self):
        return self.name

class Category(models.Model):
        name = models.CharField(max_length=100)
        #image = models.ImageField(upload_to='places/')
        def __str__(self):
            return self.name

class Proprety(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='proprety/')
    price = models.IntegerField(default=0)
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='place_prt')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_prt')
    createdat = models.DateTimeField(default=timezone.now)
    # image = models.ImageField(upload_to='places/')
    desc = models.TextField(max_length=500)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= slugify(self.name, self.pk)
            super().save(*args,**kwargs)
    def get_absolute_url (self):
        from django.urls import reverse
        return reverse('propreties:prop_detail', kwargs={'slug': self.slug})

class ImgProprety(models.Model):
    property=models.ForeignKey(Proprety, on_delete=models.CASCADE, related_name='proprety_img')
    imgfield = models.ImageField(upload_to='propretyimg/')
    def __str__(self):
        return self.property

class PropretyReview(models.Model):
        author = models.ForeignKey(User,related_name='review_auth',on_delete=models.CASCADE)
        property = models.ForeignKey(Proprety, related_name='review_propt', on_delete=models.CASCADE)
        rate = models.IntegerField(default=0)
        opp = models.TextField(max_length=200)
        createdat=models.DateTimeField(default=timezone.now)
        # image = models.ImageField(upload_to='places/')
        slug = models.SlugField(blank=True, null=True)
        def __str__(self):
            return self.property
count=((1,1),(2,2),(3,3),(4,4))
class ProtBook(models.Model):
    user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Proprety, related_name='book_propt', on_delete=models.CASCADE)
    dateFrome = models.DateField(default=timezone.now)
    dateTo = models.DateField(default=timezone.now)
    geust= models.CharField(max_length=2,choices=count)
    childrene = models.CharField(max_length=2,choices=count)
    def __str__(self):
        return  self.property