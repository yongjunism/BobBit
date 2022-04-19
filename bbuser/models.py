from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):


class Newdasdasdasdasd(models.Model):
    name = models.CharField(max_length=255)
    asdas = models.CharField()

    def __str__(self):
        return self.name
