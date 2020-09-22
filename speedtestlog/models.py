from django.db import models

# Create your models here.


class SpeedTestResult(models.Model):
    timestamp = models.DateTimeField()
    ping = models.FloatField(null=True)
    download = models.FloatField(null=True)
    upload = models.FloatField(null=True)
    json = models.JSONField()
