from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.views import View

from .models import Spot

import pyproj


class IndexView(TemplateView):
    template_name = 'tokyo_in_map/index.html'


class SpotsView(View):
    method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return render(request, 'tokyo_in_map/spots.html')

    def post(self, request):
        request_latitude = request.POST['latitude']
        request_longitude = request.POST['longitude']

        spots = self.search_spots(request_latitude, request_longitude)

        data = {
            'spots': spots
        }

        return JsonResponse(data, safe=False)

    def search_spots(self, request_latitude, request_longitude):
        spot_obj_list = Spot.objects.all()

        spots = []

        for spots_obj in spot_obj_list:
            distance_meter = self.culc_distance(request_latitude, request_longitude, spots_obj.latitude,
                                           spots_obj.longitude)

            spot = {
                'address': spots_obj.address,
                'distance_meter': distance_meter,
            }

            if spots_obj.intensity_meter > distance_meter:
                spot['content_url'] = spots_obj.content_url
            else:
                spot['content_url'] = None

            spots.append(spot)

        spots.sort(key=lambda x: x['distance_meter'])

        return spots

    def culc_distance(self, lat1, lng1, lat2, lng2):
        grs80 = pyproj.Geod(ellps='GRS80')  # GRS80楕円体
        azimuth, bkw_azimuth, distance_meter = grs80.inv(lng1, lat1, lng2, lat2)

        return distance_meter
