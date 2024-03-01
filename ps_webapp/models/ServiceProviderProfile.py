# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from . import AccountProfile

class ServiceProviderProfile(models.Model):
    pass
    # id = models.BigAutoField(primary_key=True)
    # user = models.ForeignKey('AccountProfile', models.DO_NOTHING)
    # bio = models.TextField(blank=True, null=True)
    # portfolio_url = models.CharField(max_length=200, blank=True, null=True)
    # expertise = models.CharField(max_length=100, blank=True, null=True)
    # instagram_handle = models.CharField(max_length=100, blank=True, null=True)
    # facebook_handle = models.CharField(max_length=100, blank=True, null=True)
    # twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    # profile_picture = models.CharField(max_length=100, blank=True, null=True)
    #
    # class Meta:
    #     managed = False
    #     db_table = '"general"."service_provider_profile"'
