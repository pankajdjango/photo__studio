# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserRoles(models.Model):
    uniq_id = models.AutoField(primary_key=True)
    role = models.ForeignKey('RoleMaster', models.DO_NOTHING, blank=True, null=True)
    userid = models.ForeignKey('AccountProfile', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    generated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"general"."user_roles"'
