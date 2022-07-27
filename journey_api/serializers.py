from rest_framework import serializers
from journey_model.models import Journey, Station

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ('id', 'departure_date', 'return_date', 'departure_station_id', 'departure_station_name', 'return_station_id', 'return_station_name', 'covered_distance', 'duration')

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'station_id', 'name_finnish', 'name_swedish', 'name_english', 'address_finnish', 'address_swedish', 'city_finnish', 'city_swedish', 'operator', 'capacity', 'coordinate_x', 'coordinate_y')