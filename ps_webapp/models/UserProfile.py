from django.db import models


class UserProfile(models.Model):
    pass
    # id = models.BigAutoField(primary_key=True)
    # organization_name = models.CharField(max_length=255, blank=True, null=True)
    # organization_type = models.CharField(max_length=100, blank=True, null=True)
    # website = models.CharField(max_length=200, blank=True, null=True)
    # bio = models.TextField(blank=True, null=True)
    # profile_picture = models.CharField(max_length=100, blank=True, null=True)
    # userid = models.ForeignKey('AccountProfile', models.DO_NOTHING, db_column='userid')

    # class Meta:
    #     managed = False
    #     db_table = '"general"."user_profile"'
