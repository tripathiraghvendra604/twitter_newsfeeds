from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class News(models.Model):
    tag = models.CharField(max_length=100)
    heading = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True, auto_now= False)
    link = models.CharField(max_length=200)
    country = models.ForeignKey(Country)
    image_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.tag
