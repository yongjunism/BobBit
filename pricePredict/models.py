from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField, DateField
from django.conf import settings
from sqlalchemy import Float
from bbuser.models import User


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
    nextprice = IntegerField(default=0)
    percent = FloatField(default=0)
    pSearchcount = IntegerField(default=0)
    pWishcount = IntegerField(default=0)
    RMSE = FloatField(default=0, null=True)
    pImage = CharField(max_length=255, null=True)
    cKey = models.ForeignKey(
        Categori, on_delete=models.CASCADE, db_column='cKey', null=True)

    wish_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='wish_user'
    )

    def count_wish_user(self):
        return self.wish_user.count()

    class Meta:
        db_table = 'Product'


class VirtualProduct(models.Model):

    userID = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, db_column='user_id')
    pNo = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='pNo', null=True)
    pNum = IntegerField(default=1)

    class Meta:
        db_table = 'VirtualProduct'
