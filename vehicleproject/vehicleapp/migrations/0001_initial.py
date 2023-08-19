# Generated by Django 4.2.1 on 2023-08-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_company', models.CharField(max_length=30)),
                ('bike_color', models.CharField(max_length=30)),
                ('bike_fuel_type', models.CharField(max_length=10)),
                ('bike_milage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_company', models.CharField(max_length=30)),
                ('car_color', models.CharField(max_length=30)),
                ('car_fuel_type', models.CharField(max_length=10)),
                ('car_milage', models.IntegerField()),
            ],
        ),
    ]