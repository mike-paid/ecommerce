from django.db import models
from .manager import CustomizeUser
from django.contrib.auth.models import AbstractUser
# Create your models here.


class user(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="profile")
    phone = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = CustomizeUser()