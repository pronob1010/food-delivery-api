from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        # if not email:
            # raise ValueError()
        pass

    def create_superuser(self, email, password, **extra_fields):
        pass