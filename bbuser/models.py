from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

import os


def content_file_name(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join("profile", filename)


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    profile_img = models.ImageField(null=True, upload_to=content_file_name,
                                    blank=True)
    point = models.IntegerField(default=0)
    first_name = None
    first_login = models.IntegerField(default=0)
    last_login2 = models.DateTimeField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
