from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core import serializers
from .models import Itinerary
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_itineraries(request):
    if request.method == 'GET':
        agent_name = request.GET.get('agent_name', None)
        itineraries = Itinerary.objects.all()
        if agent_name:
            itineraries = itineraries.filter(agent__name__contains=agent_name)
        print(itineraries[0].legs.all())
        serialized_itineraries = map(json_itinerary, itineraries)
        return Response({'data': serialized_itineraries}, status=200)

def json_itinerary(itinerary):
    return {
        'id': itinerary.id,
        'legs': map(json_leg,itinerary.legs.all()),
        'price': f'{itinerary.currency}{itinerary.price}',
        'agent': {
            'id': itinerary.agent.id,
            'name': itinerary.agent.name,
            'rating': itinerary.agent.rating,
        }
    }


def json_leg(leg):
    return {
        'id': leg.id,
        'departure_airport': leg.departure_airport,
        'arrival_airport':  leg.arrival_airport,
        'departure_time':  leg.departure_time,
        'arrival_time':  leg.arrival_airport,
        'stops': leg.stops,
        'airline': {
            "id": leg.airline.id,
            "name": leg.airline.name,
            "airline_id": leg.airline.airline_id
        },
        'duration_mins': leg.duration_mins,
        }
