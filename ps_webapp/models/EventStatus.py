from django.db import models

        
class EventStatus(models.Model):
    status = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = '"general"."event_status"'


