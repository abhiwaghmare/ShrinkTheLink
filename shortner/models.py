from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    original_url= models.URLField(blank=False,default='')
    short_query= models.CharField(blank=True,max_length=8)