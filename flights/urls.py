from django.urls import path
from . import views

urlpatterns = [
    path('itineraries', views.get_itineraries )
]