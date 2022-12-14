import email
from enum import Flag, unique
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager 
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provider"))
        email = self.normalize_email(email)

        new_user = self.model(email= email, **extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_supperuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Supperuser should have is staff as true."))

        if extra_fields.get('is_supperuser') is not True:
            raise ValueError(_("Supperuser should have is supperuser as true."))
            
        if extra_fields.get('is_asctive') is not True:
            raise ValueError(_("Supperuser should have is active as true."))
        
        return self.create_user(email,password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"