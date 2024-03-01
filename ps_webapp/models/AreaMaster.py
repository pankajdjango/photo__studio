# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaMaster(models.Model):
    area_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    area_code = models.CharField(max_length=6)
    city = models.ForeignKey('CityMaster', models.DO_NOTHING, blank=True, null=True)
    address_matched = models.IntegerField(blank=True, null=True)
    test_col = models.IntegerField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = '"general"."area_master"'
