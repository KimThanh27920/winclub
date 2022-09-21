from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email:
            raise(ValueError('email is required'))
        if not phone:
            raise ValueError('phone number is required')

        user=self.model(
            email = email,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None):
        user=self.create_user(
            email = email,
            phone = phone,
            password = password
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, null=True)
    birtday = models.CharField(max_length=255)
    gender = models.BooleanField(default=True)
    points = models.IntegerField(default=0)
    stripe_account = models.CharField(max_length=255)

    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_business = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'full_name']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Pin(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    pin = models.IntegerField()