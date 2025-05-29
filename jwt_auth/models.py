
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)  
    otp = models.CharField(max_length=6, blank=True, null=True)
