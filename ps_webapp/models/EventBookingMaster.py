from django.db import models


class EventBookingMaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.ForeignKey('CityMaster', models.DO_NOTHING, db_column='city', blank=True, null=True)
    event = models.ForeignKey('EventType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AccountProfile', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    area_address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    event_date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    status = models.ForeignKey('EventStatus', models.DO_NOTHING, db_column='status',default="Pending")
    is_confirmed = models.BooleanField(blank=True, null=True,default=False)
    generated = models.IntegerField(blank=True, null=True)
    updated_on = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."event_booking_master"'
    def __str__(self):
        return f"{self.event.event_name} : {self.event_date}"
