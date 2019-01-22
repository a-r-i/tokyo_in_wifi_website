from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.views import View

from tokyo_in_map.services import search_spots


class IndexView(TemplateView):
    template_name = 'tokyo_in_map/index.html'


class SpotsView(View):
    method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return render(request, 'tokyo_in_map/spots.html')

    def post(self, request):
        print(request.POST)

        request_latitude = request.POST['latitude']
        request_longitude = request.POST['longitude']
        try:
            request_count = int(request.POST['count'])
        except KeyError:
            request_count = 100

        spots = search_spots(request_latitude, request_longitude, request_count)

        data = {
            'spots': spots
        }

        return JsonResponse(data, safe=False)