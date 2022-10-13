from enum import auto
from pyexpat import model
from django.db import models

# Create your models here.
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.test import modify_settings
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

#abstracebaseuser
class User(AbstractUser): 
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)
        