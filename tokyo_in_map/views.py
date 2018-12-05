from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Spot

import pyproj


def index(request):
    return render(request, 'tokyo_in_map/index.html')


@ensure_csrf_cookie
def spots(request):
    if request.method == 'POST':
        request_latitude = request.POST['latitude']
        request_longitude = request.POST['longitude']

        spots = search_spots(request_latitude, request_longitude)

        data = {
            'spots':spots
        }

        return JsonResponse(data, safe=False)
    else:
        return render(request, 'tokyo_in_map/spots.html')


# model.pyに書くべき処理？
def search_spots(request_latitude, request_longitude):
    spot_obj_list = Spot.objects.all()

    spots = []

    for spots_obj in spot_obj_list:
        distance = culc_distance(request_latitude, request_longitude, spots_obj.latitude, spots_obj.longitude)

        spot = {
            'address': spots_obj.address,
            'distance': distance,
        }

        INTENSITY_METER = 50 # WiFiスポットの何メートル以内なら、WiFiに接続できるか

        if INTENSITY_METER > distance:
            spot['content_url'] = spots_obj.content_url
        else:
            spot['content_url'] = None

        spots.append(spot)

    spots.sort(key=lambda x: x['distance'])

    return spots


def culc_distance(lat1, lng1, lat2, lng2):
    grs80 = pyproj.Geod(ellps='GRS80')  # GRS80楕円体
    azimuth, bkw_azimuth, distance_meter = grs80.inv(lng1, lat1, lng2, lat2)

    return distance_meter