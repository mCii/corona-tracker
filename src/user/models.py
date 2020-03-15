from random import randrange

import re
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import SET_NULL, ForeignKey

from common.behaviours import UUIDable, Timestampable


class UserManager(BaseUserManager):
    def update_or_create_user(self, email=None, password=None, **extra_fields):
        email = self.normalize_email(email)
        try:
            user = self.get(email=email)
            for key, value in extra_fields.items():
                setattr(user, key, value)
        except User.DoesNotExist:
            user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self.update_or_create_user(email, password, **extra_fields)

    def create_user(self, email):
        extra_fields = {'is_patient': True}
        return self.update_or_create_user(email, **extra_fields)


class City(UUIDable, models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.uuid

    def generate_uuid(self):
        name = re.sub(r'\W+', '_', self.name).lower()
        return f'city_{name}'

    class Meta:
        verbose_name_plural = 'cities'


class Nationality(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'nationalities'


class User(UUIDable, Timestampable, AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    objects = UserManager()

    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    first_name = models.CharField('first name', max_length=30, blank=True, default='')
    last_name = models.CharField('last name', max_length=30, blank=True, default='')
    is_patient = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=24, null=True, blank=True)
    identity_card_number = models.CharField(max_length=24, null=True, blank=True)
    passport_number = models.CharField(max_length=24, null=True, blank=True)
    nationality = ForeignKey(Nationality, null=True, blank=True, on_delete=SET_NULL)
    age = models.IntegerField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.uuid

    def generate_uuid(self) -> str:
        first_name = re.sub(r'\W+', '_', self.first_name).lower()
        last_name = re.sub(r'\W+', '_', self.last_name).lower()
        random_number = randrange(1000)
        random_number = str(random_number).zfill(4)
        return f'user_{first_name}_{last_name}_{random_number}'
