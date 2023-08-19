from django.db import models

# Create your models here.
class cars(models.Model):
    car_company=models.CharField(max_length=30)
    car_color=models.CharField(max_length=30)
    car_fuel_type=models.CharField(max_length=10)
    car_milage=models.IntegerField()
class bikes(models.Model):
    bike_company=models.CharField(max_length=30)
    bike_color=models.CharField(max_length=30)
    bike_fuel_type=models.CharField(max_length=10)
    bike_milage=models.IntegerField()
