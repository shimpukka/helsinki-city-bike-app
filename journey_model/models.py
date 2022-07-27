from django.db import models

# Create your models here.
class Journey (models.Model):
    departure_date = models.CharField(max_length=50)
    return_date = models.CharField(max_length=50)
    departure_station_id = models.IntegerField()
    departure_station_name = models.CharField(max_length=50)
    return_station_id = models.IntegerField()
    return_station_name = models.CharField(max_length=50)
    covered_distance = models.IntegerField()
    duration = models.IntegerField()

    objects = models.Manager() #default manager

class Station (models.Model): 

    station_id = models.IntegerField()
    name_finnish = models.CharField(max_length=50)
    name_swedish = models.CharField(max_length=50)
    name_english = models.CharField(max_length=50)
    address_finnish = models.CharField(max_length=50)
    address_swedish = models.CharField(max_length=50)
    city_finnish = models.CharField(max_length=50)
    city_swedish = models.CharField(max_length=50)
    operator = models.CharField(max_length=50)
    capacity = models.IntegerField()
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()

    stationObjects = models.Manager()