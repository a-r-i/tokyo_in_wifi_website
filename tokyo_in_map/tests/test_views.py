from django.test import TestCase

class TestIndexView(TestCase):
    def test_get(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tokyo_in_map/index.html')


class TestSpotsView(TestCase):
    fixtures = ['test_views.json']

    def test_get(self):
        response = self.client.get('/spots')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tokyo_in_map/spots.html')

    def test_post(self):
        data = {
            'latitude': 35.6895924,
            'longitude': 139.7004131
        }
        response = self.client.post('/spots', data)
        self.assertEquals(response.status_code, 200)