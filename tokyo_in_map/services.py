import logging

import pyproj

from .models import Spot, Content

logging.getLogger(__name__)


def search_spots(request_latitude, request_longitude, request_count):
    spots = []

    spot_obj_list = Spot.objects.all()

    for spot_obj in spot_obj_list:
        distance_meter = culc_distance(request_latitude, request_longitude, spot_obj.latitude,
                                            spot_obj.longitude)

        spot = {
            'address': spot_obj.address,
            'distance_meter': distance_meter,
            'content_url': None
        }

        if spot_obj.intensity_meter > distance_meter:
            try:
                content_obj = Content.objects.get(spot=spot_obj.id)
            except Content.DoesNotExist:
                logging.error('Content.DoesNotExist')
            else:
                spot['content_url'] = content_obj.content_url

        spots.append(spot)

    spots.sort(key=lambda x: x['distance_meter'])
    sliced_spots = spots[0:request_count]

    return sliced_spots


def culc_distance(lat1, lng1, lat2, lng2):
    grs80 = pyproj.Geod(ellps='GRS80')  # GRS80楕円体
    azimuth, bkw_azimuth, distance_meter = grs80.inv(lng1, lat1, lng2, lat2)

    return distance_meter