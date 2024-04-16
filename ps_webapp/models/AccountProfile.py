from django.db import models
from ps_webapp.models import CityMaster


class AccountProfile(models.Model):
    userid = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True, max_length=254, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, blank=True, null=True)
    generated = models.IntegerField(blank=True, null=True)
    updated_on = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey('CityMaster', models.DO_NOTHING, db_column='city', blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    profile_photo = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = '"general"."account_profile"'

    def __str__(self):
        return self.full_name
