from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField
from django.conf import settings
# Create your models here.


class Categori(models.Model):
    cKey = IntegerField(primary_key=True)
    pCategory = CharField(max_length=30)
    cSearchCount = IntegerField(default=0)

    class Meta:
        db_table = 'Categori'


class Product(models.Model):
    pNo = IntegerField(primary_key=True)
    pName = CharField(max_length=30)
    price = IntegerField(default=0)
    pSearchcount = IntegerField(default=0)
    pWishcount = IntegerField(default=0)
    pLink = CharField(max_length=255, null=True)
    pImage = CharField(max_length=255, null=True)
    cKey = models.ForeignKey(
        Categori, on_delete=models.CASCADE, db_column='cKey', null=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    wish_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='wish_user'
    )

    def count_wish_user(self):
        return self.pWishcount.count()

    class Meta:
        db_table = 'Product'
