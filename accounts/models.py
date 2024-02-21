from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(null=False, blank=False, max_length=300)
    phone_number = models.CharField(null=False, blank=False, max_length=10)
