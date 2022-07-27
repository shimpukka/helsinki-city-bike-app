from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from journey_model.models import Journey, Station
from .serializers import JourneySerializer, StationSerializer

# Create your views (request handler) here.

class JourneyList(generics.ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    pass 

class JourneyDetail(generics.RetrieveDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    pass 

class StationList(generics.ListCreateAPIView):
    queryset = Station.stationObjects.all()
    serializer_class = StationSerializer
    pass 

class StationDetail(generics.RetrieveDestroyAPIView):
    queryset = Station.stationObjects.all()
    serializer_class = StationSerializer
    pass 