from django.db import models


class Stockdb(models.Model):
    stock_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StockDB'


class Issuedb(models.Model):
    issue_id = models.AutoField(primary_key=True, blank=True, null=False)
    issue = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IssueDB'


class Newsdb(models.Model):
    news_id = models.AutoField(primary_key=True, blank=True, null=False)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NewsDB'


