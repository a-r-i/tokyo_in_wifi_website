from django.test import TestCase

class TestIndexView(TestCase):
    def test_get(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tokyo_in_map/index.html')


class TestSpotsView(TestCase):
    fixtures = ['test_views.json']

    def setUp(self):
        # 新宿駅の緯度と経度
        self.data = {
            'latitude': 35.6895924,
            'longitude': 139.7004131
        }

    def test_get(self):
        response = self.client.get('/spots')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tokyo_in_map/spots.html')

    def test_post_response_status_code_200(self):
        response = self.client.post('/spots', self.data)
        self.assertEquals(response.status_code, 200)

    # spotsリストは要素を持っているか
    def test_spots_has_element(self):
        response = self.client.post('/spots', self.data)
        response_json = response.json()
        spots = response_json['spots']
        self.assertTrue(spots != [])