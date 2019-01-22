from django.test import TestCase
from ..services import search_spots, culc_distance


class TestSearchSpots(TestCase):

    def setUp(self):
        # 新宿駅の緯度と経度
        self.latitude = 35.6895924
        self.longitude = 139.7004131
        self.count = 100

    def test_spots_is_instance_list(self):
        spots = search_spots(self.latitude, self.longitude, self.count)
        self.assertIsInstance(spots, list)


class TestCulcDistance(TestCase):

    def setUp(self):
        # 新宿駅の緯度と経度
        self.lat1 = 35.6895924
        self.lng1 = 139.7004131
        # 東京駅の緯度と経度
        self.lat2 = 35.681467
        self.lng2 = 139.767184

    def test_distance_meter_is_instance_float(self):
        distance_meter = culc_distance(self.lat1, self.lng1, self.lat2, self.lng2)
        self.assertIsInstance(distance_meter, float)