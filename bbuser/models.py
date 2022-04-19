from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    test = models.CharField(max_length=20, default="")
    test2 = models.CharField(max_length=20, null=True)
    first_name = None
