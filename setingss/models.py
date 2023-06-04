from django.db import models

class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    descri = models.TextField(max_length=50)
    logo = models.ImageField(upload_to='about/')
    fb_link = models.URLField()

    def __str__(self):
        return self.site_name