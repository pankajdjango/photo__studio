# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PincodeMaster(models.Model):
    office_name = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    office_type = models.CharField(max_length=10, blank=True, null=True)
    delivery_status = models.CharField(max_length=100, blank=True, null=True)
    division_name = models.CharField(max_length=200, blank=True, null=True)
    region_name = models.CharField(max_length=100, blank=True, null=True)
    circle_name = models.CharField(max_length=100, blank=True, null=True)
    taluk_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode_id = models.AutoField(primary_key=True)
    city_0 = models.ForeignKey('CityMaster', models.DO_NOTHING, db_column='city_id')  # Field renamed because of name conflict.
    area = models.ForeignKey('AreaMaster', models.DO_NOTHING, blank=True, null=True)
    office_name_short = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."pincode_master"'
