from django.db import models

# Create your models here.
class Stock(models.Model):

#     id = models.AutoField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    listing_date = models.TextField(blank=True, null=True)
    settlement_month = models.TextField(blank=True, null=True)
    representative = models.TextField(blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'