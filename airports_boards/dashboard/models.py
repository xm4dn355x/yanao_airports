from django.db import models

# Create your models here.

class Flights(models.Model):
    orig_airport = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=10)
    flight = models.CharField(max_length=30)
    dest_airport = models.CharField(max_length=100)
    plane = models.CharField(max_length=100)
    plan_time = models.CharField(max_length=20)
    fact_time = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
