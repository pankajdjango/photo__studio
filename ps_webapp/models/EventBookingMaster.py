from django.db import models


class EventBookingMaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.ForeignKey('CityMaster', models.DO_NOTHING, db_column='city', blank=True, null=True)
    event = models.ForeignKey('EventType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AccountProfile', models.DO_NOTHING, db_column='userid', blank=True, null=True, related_name='event_booking_user')
    area_address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    event_date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    status = models.ForeignKey('EventStatus', models.DO_NOTHING, db_column='status',default="Pending")
    generated = models.IntegerField(blank=True, null=True)
    updated_on = models.IntegerField(blank=True, null=True)
    updated_by = models.ForeignKey('AccountProfile', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='event_booking_updated_by')

    class Meta:
        managed = False
        db_table = '"general"."event_booking_master"'

    def __str__(self):
        return f"{self.event.event_name} : {self.event_date}"
