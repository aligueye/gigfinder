from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    # function to create user
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    # function to create superuser
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser):

    ROLE_CHOICES = (
        ('tasker', 'Tasker'),
        ('poster', 'Poster'),
    )

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='poster')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    