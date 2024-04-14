from django.db import models

class EventType(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = '"general"."event_type"'
