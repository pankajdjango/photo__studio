from django.db import models

import datetime
class UrlHistory(models.Model):
    userid = models.ForeignKey('AccountProfile', models.DO_NOTHING, db_column='userid')
    # url_visited = models.CharField(max_length=100, blank=True, null=True)
    url_visited = models.TextField(blank=True, null=True)
    generated = models.IntegerField(null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"general"."url_history"'

    def __str__(self):
        generated = datetime.datetime.fromtimestamp(self.generated)
        return f'{self.userid} : {self.url_visited} : {generated}'
