from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.validators import RegexValidator
from django.db import models

from utils.models import BaseModel


username_validator = RegexValidator(
    regex=r'^[\w]+$',
    message='Enter a valid username. Username may contain only up to 30 letters and numbers.'
)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    username = models.CharField(
        max_length=30,
        unique=True,
        help_text= 'Required. 30 characters or fewer. Letters, digits only.',
        validators=[
            username_validator
        ],
        error_messages={
            'unique': 'A user with that username already exists.'
        })

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=64)

    objects = UserManager()


# Register the signal listeners.
from . import listeners  # noqa: F401