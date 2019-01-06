from .models import Spot

import pyproj

def search_spots(request_latitude, request_longitude):
    spot_obj_list = Spot.objects.all()

    spots = []

    for spots_obj in spot_obj_list:
        distance_meter = culc_distance(request_latitude, request_longitude, spots_obj.latitude,
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


def culc_distance(lat1, lng1, lat2, lng2):
    grs80 = pyproj.Geod(ellps='GRS80')  # GRS80楕円体
    azimuth, bkw_azimuth, distance_meter = grs80.inv(lng1, lat1, lng2, lat2)

    return distance_meter