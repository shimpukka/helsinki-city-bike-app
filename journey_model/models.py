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