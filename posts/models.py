from datetime import datetime

from django.db import models


# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    pic = models.CharField(default = 'water', max_length=20)
