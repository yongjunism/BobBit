# from django.db import models
# from django.contrib.auth.models import User


# # Extending User Model Using a One-To-One Link
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username
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