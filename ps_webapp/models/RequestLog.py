from django.db import models


class RequestLog(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, null=True)
    path = models.TextField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(blank=True, null=True)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    os_system = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    additional_info = models.JSONField(null=True, blank=True)
    generated = models.IntegerField()

    class Meta:
        managed = False
        db_table = '"general"."request_log"'