from django.db import models

class About(models.Model):
    what_do = models.TextField(max_length=1000)
    our_miss = models.TextField(max_length=1000)
    our_goal = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='about/')

    def __str__(self):
        return str(self.id)
class Faq (models.Model):
        titel = models.CharField(max_length=160)
        descr = models.TextField(max_length=1000)

        def __str__(self):
            return self.titel
