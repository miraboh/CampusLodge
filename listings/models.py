from django.db import models
from datetime import datetime
from agents.models import Agent


class Listing(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    campus_school = models.CharField(max_length=200)
    locality_name = models.CharField(max_length=200)
    house_title = models.CharField(max_length=200)
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    block_number = models.CharField(max_length=100)
    house_type = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.house_title
