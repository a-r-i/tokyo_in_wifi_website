from django.db import models


class Spot(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100, null=True)
    intensity_meter = models.IntegerField(default=50) # スポットに何メートルまで近づけばWiFiを受信できるか
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Content(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.PROTECT)
    content_url = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)