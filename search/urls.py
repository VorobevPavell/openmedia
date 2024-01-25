from django.urls import path
from .views import SearchByPlateNumberView, SearchByVinView


urlpatterns = [
    path('', SearchByPlateNumberView.as_view(), name="plate_number"),
    path('plate-number/', SearchByPlateNumberView.as_view(), name="plate_number"),
    path('vin/', SearchByVinView.as_view(), name="vin"),
]