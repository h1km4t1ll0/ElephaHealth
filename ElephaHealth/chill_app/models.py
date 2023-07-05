from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.validators import ASCIIUsernameValidator


class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    first_name = models.CharField(max_length=30)  # name
    last_name = models.CharField(max_length=30)  # surname
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    date_of_birth = models.DateField()  # date of birth

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    height = models.FloatField()
    weight = models.FloatField()
    avg_heart_rate = models.IntegerField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'company', 'phone_number', 'gender',
                       'height', 'weight', 'avg_heart_rate']

    def __str__(self):
        return self.username


# Исследование состояния пользователя
class Analysis(models.Model):
    person = models.ForeignKey(User, related_name='analysis', on_delete=models.CASCADE)
    # Надо решить, удаляем ли мы исследования после удаления пользователя. Пока что - да. Иначе - изменить CASCADE.

    hr_before = models.IntegerField()
    hr_after = models.IntegerField()
    condition = models.CharField(max_length=30)
