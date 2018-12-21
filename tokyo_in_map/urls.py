from django.urls import path

from. import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('spots', views.SpotsView.as_view()),
]