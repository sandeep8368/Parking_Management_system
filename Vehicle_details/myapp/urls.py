from django.urls import path
from .views import get_vehicle_info

urlpatterns = [
    path('vehicle-info/', get_vehicle_info, name='vehicle-info'),
]
