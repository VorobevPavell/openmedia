from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from search.functions import search_vehicle_info


class SearchByPlateNumberView(View):

    @staticmethod
    def get(request):
        return render(request, "plate_number.html")

    @staticmethod
    def post(request):
        data = request.POST
        plate_number = data['plate_number']
        try:
            result = search_vehicle_info("num_plate", plate_number)
            result[0] = result[0].split('\n')[:-13]
        except Exception:
            SearchByPlateNumberView.post(request)
        return HttpResponse(result)


class SearchByVinView(View):

    @staticmethod
    def get(request):
        return render(request, "vin.html")

    @staticmethod
    def post(request):
        data = request.POST
        vin = data["vin"]
        try:
            result = search_vehicle_info("vin", vin)
            result[0] = result[0].split('\n')[:-13]
        except Exception:
            SearchByVinView.post(request)
        return HttpResponse(result)
