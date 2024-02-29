from django.db import models

class CountryMaster(models.Model):
    country_code = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(unique=True, max_length=100)
    risk_level = models.CharField(max_length=20)
    isd_code = models.IntegerField(blank=True, null=True)
    cr_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cr_price_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    continent = models.CharField(max_length=50, blank=True, null=True)
    record_type = models.CharField(max_length=30)
    im_contact = models.BooleanField(blank=True, null=True)
    sms_allowed = models.BooleanField(blank=True, null=True)
    neighbour_countries = models.TextField(blank=True, null=True)  # This field type is a guess.
    name_hi = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = '"general"."country_master"'


class CountryStates(models.Model):
    state = models.CharField(primary_key=True, max_length=80)
    country_code = models.ForeignKey('CountryMaster', models.DO_NOTHING, db_column='country_code')
    state_abbrev = models.CharField(max_length=10, blank=True, null=True)
    state_id = models.AutoField(unique=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    gst_state_code = models.IntegerField(blank=True, null=True)
    alpha_code = models.CharField(max_length=7, blank=True, null=True)
    state_hi = models.TextField(blank=True, null=True)
    for_gst = models.BooleanField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = '"general"."country_states"'
        unique_together = (('state', 'country_code'),)


class CityMaster(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    area_code = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=2)
    state = models.ForeignKey('CountryStates', models.DO_NOTHING, db_column='state')
    population = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    admin = models.CharField(max_length=1, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    time_offset = models.FloatField(blank=True, null=True)
    audit_date_created = models.DateTimeField(blank=True, null=True)
    audit_date_modified = models.DateTimeField(blank=True, null=True)
    audit_version = models.IntegerField(blank=True, null=True)
    models.IntegerField(blank=True, null=True)
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
