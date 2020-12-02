from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

Gender_CHOICES = (
    ('M', ("Male")),
    ('F', ("Female"))
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(default=0)
    alt_no = models.IntegerField(default=0)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    gender = models.CharField(choices = Gender_CHOICES,max_length=1)
    pincode = models.IntegerField(default=0)
    photo = models.ImageField(upload_to ='user/')



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class State(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)


    def __str__(self):
        return self.name
