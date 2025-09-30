from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, phone=None, name='', address='', **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        if not email:
            raise ValueError('The email must be set')
        if not phone:
            raise ValueError('The phone must be set')
        if not name:
            raise ValueError('The name must be set')

        email = self.normalize_email(email)
        username = username.strip()
        user = self.model(
            username=username,
            email=email,
            phone=phone,
            name=name,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, phone=None, name='', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            username=username,
            email=email,
            password=password,
            phone=phone,
            name=name,
            **extra_fields
        )


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=150)
    address = models.TextField(blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
