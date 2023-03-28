from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required'))
        
        email = self.normalize_email(email)
        new_user = self.model(email = email, **extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=50,
    null = False,
     blank = False,
     help_text = _('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
     verbose_name = _('Username'),)

    email = models.EmailField(
        null = False,
        unique = True,
        blank = False,
        verbose_name = _('Email'),
        help_text = _('Required. 254 characters or fewer.Follows email format: john.doe@mail.com'),
    )
    phone_number = PhoneNumberField(null=True,
     blank=True,
     verbose_name='Phone Number',
     help_text='Follow phone number format: +1 123 456 7890')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    objects = CustomUserManager()

    def __str__(self):
        return self.email
