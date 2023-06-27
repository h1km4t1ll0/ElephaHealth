from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254)
    company = models.CharField(max_length=30)
    dob = models.DateField()  # date of birth

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    height = models.FloatField()
    weight = models.FloatField()
    avg_heart_rate = models.IntegerField()


class Analysis(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    hr_before = models.IntegerField()
    hr_after = models.IntegerField()
    condition = models.CharField(max_length=30)
