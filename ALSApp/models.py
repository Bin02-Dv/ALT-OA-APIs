from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthApiModel(AbstractUser):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    email = models.CharField(max_length=225, unique=True)
    username = None
    password = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=225, unique=True)
    invitation_code = models.CharField(max_length=225)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
