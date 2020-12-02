from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = PhoneNumberField(
        blank=True, null=True, region='IN')
    company_website = models.CharField(max_length=80, blank=True)
    company_challenge = models.CharField(max_length=180, blank=True)
    project_briefly = models.TextField(blank=True)
    budget = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
