# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CityMaster(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    area_code = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=2)
    # state = models.ForeignKey('CountryStates', models.DO_NOTHING, db_column='state')
    state = models.ForeignKey('CountryStates', models.DO_NOTHING, db_column='state', to_field='state')
    population = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    admin = models.CharField(max_length=1, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    time_offset = models.FloatField(blank=True, null=True)
    audit_date_created = models.DateTimeField(blank=True, null=True)
    audit_date_modified = models.DateTimeField(blank=True, null=True)
    audit_version = models.IntegerField(blank=True, null=True)
    audit_id = models.IntegerField(blank=True, null=True)
    city_synonym = models.CharField(max_length=100, blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    longitude_float = models.FloatField(blank=True, null=True)
    latitude_float = models.FloatField(blank=True, null=True)
    top_city = models.BooleanField(blank=True, null=True)
    search_city = models.BooleanField()
    seo_city_id = models.IntegerField(blank=True, null=True)
    covid_zone = models.CharField(max_length=50, blank=True, null=True)
    hindi_city = models.CharField(max_length=150, blank=True, null=True)
    city_hi = models.TextField(blank=True, null=True)
    state_hi = models.TextField(blank=True, null=True)
    city_tier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."city_master"'
        unique_together = (('city', 'state', 'country_code'),)
