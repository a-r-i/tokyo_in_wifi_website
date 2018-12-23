from django.urls import path

from. import views

urlpatterns = [
    path('', views.SpotsView.as_view()),
]