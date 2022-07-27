from django.urls import path
from . import views
from .views import JourneyList, JourneyDetail, StationList, StationDetail

#URLConf
urlpatterns = [
    path('journey/<int:pk>/', JourneyDetail.as_view()),
    path('journey/', JourneyList.as_view()),
    path('station/', StationList.as_view()),
    path('station/<int:pk>/', StationDetail.as_view())
]