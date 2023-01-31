
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator,RegexValidator,EmailValidator
from django.db import models


# Create your models here.

def is_mail_valid(value):
    if not str(value).endswith("@esprit.tn"):
        raise ValidationError("Email must be an esprit email")

class Person(AbstractUser):
    cin = models.CharField(
        "CIN",
        primary_key=True,
        max_length=8

        , validators=[MaxLengthValidator(8, message="verify length"), MinLengthValidator(8),RegexValidator(r'^[0-9]*$')]
    )
    username = models.CharField("Username", max_length=255, unique=True)
    email = models.EmailField(
        unique=True,validators=[is_mail_valid]
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "users"
