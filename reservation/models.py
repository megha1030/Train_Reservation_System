from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    # username = models.TextField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    # password = models.TextField(max_length=100)

class Train(models.Model):
    name = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    price_sleeper = models.DecimalField(max_digits=6, decimal_places=2)
    price_3ac = models.DecimalField(max_digits=6, decimal_places=2)
    price_2ac = models.DecimalField(max_digits=6, decimal_places=2)
    price_1ac = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    travel_class = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    journey_date = models.DateField(null=False)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket {self.id} for {self.user.username}'



