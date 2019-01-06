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
        print(request.method)
        return render(request, 'tokyo_in_map/spots.html')

    def post(self, request):
        request_latitude = request.POST['latitude']
        request_longitude = request.POST['longitude']

        spots = search_spots(request_latitude, request_longitude)

        data = {
            'spots': spots
        }

        return JsonResponse(data, safe=False)