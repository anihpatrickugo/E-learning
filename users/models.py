from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# User model For Lecturer and Student
class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_lecturer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


#Student model
class StudentUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    registration_number = models.IntegerField(unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "registration_number"
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
