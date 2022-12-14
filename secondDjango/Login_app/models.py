from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# User, Pass , Email 





#  for user bio, pic

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relation
    fb_id = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to= 'profile_pic', blank=True)

    def __STR__(self):
        return self.user.username # it will show username field in user model



