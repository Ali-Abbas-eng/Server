from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(null=False, blank=False, max_length=200)
    first_name = models.CharField(null=False, blank=False, max_length=200)
    last_name = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(null=False, blank=False, max_length=300, unique=True)
    phone_number = models.CharField(null=False, blank=False, max_length=10)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save()
