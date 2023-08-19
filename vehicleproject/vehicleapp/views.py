from django.shortcuts import render



from vehicleapp.models import cars

from vehicleapp.models import bikes

from vehicleapp.forms import bikesform

from vehicleapp.forms import carsform



def cars_view(request):
    cars_list=cars.objects.all()
    my_dict={'cars_list':cars_list}
    return render(request,'vehicleapp/cars.html',context=my_dict)
def bikes_view(request):
    bikes_list=bikes.objects.all()
    my_dict={'bikes_list':bikes_list}
    return render(request,'vehicleapp/bikes.html',context=my_dict)
def add_bike(request):
    form=bikesform()
    if request.method=='POST':
        form=bikesform(request.POST)
    if form.is_valid():
        form.save()
    my_dict={'form':form}
    return render(request,'vehicleapp/addbike.html',context=my_dict)
def add_car(request):
    form=carsform()
    if request.method=='POST':
        form=carsform(request.POST)
    if form.is_valid():
        form.save()
    my_dict={'form':form}
    return render(request,'vehicleapp/addcar.html',context=my_dict)
def index(request):
    return render(request,'vehicleapp/index.html')