from django.db import models
from datetime import datetime


class Agent(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about_agent = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    is_best = models.BooleanField(default=False)
    joined_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
