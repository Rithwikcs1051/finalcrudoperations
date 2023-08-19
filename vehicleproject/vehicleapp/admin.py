
from django.contrib import admin

from vehicleapp.models import cars

from vehicleapp.models import bikes


# Register your models here.
class carsadmin(admin.ModelAdmin):
    list_display=['car_company','car_color','car_fuel_type','car_milage']
admin.site.register(cars,carsadmin)
class bikesadmin(admin.ModelAdmin):
    list_display=['bike_company','bike_color','bike_fuel_type','bike_milage']
admin.site.register(bikes,bikesadmin)