from django.db import models

import pyproj

class Spot(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address =  models.CharField(max_length=100, null=True)
    content_url = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
