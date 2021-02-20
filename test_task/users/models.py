from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """CustomUser"""
    fullname = models.CharField('fullname', max_length=150)

    def __str__(self):
        return self.username

