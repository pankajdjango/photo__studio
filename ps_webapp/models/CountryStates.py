from django.db import models


class CountryStates(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=80, unique=True)  # Ensure uniqueness
    country_code = models.ForeignKey('CountryMaster', models.DO_NOTHING, db_column='country_code', blank=True, null=True, related_name='countrystates_country_code')
    state_abbrev = models.CharField(max_length=10, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."country_states"'
        unique_together = (('state', 'country_code'),)
