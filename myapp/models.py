from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')             #we need Pillow module to work with images in django
    date = models.DateTimeField(auto_now_add=True)              #this will add real time
    