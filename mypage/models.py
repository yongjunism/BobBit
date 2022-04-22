from django.db import models
from django.conf import settings
import os

def content_file_name(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join("profile", filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User모델과 Profile을 1:1로 연결
    nickname = models.CharField(max_length=20)
    profile_img = models.ImageField(null=True, blank=True)
    point = models.IntegerField(default=0)
    first_name = None