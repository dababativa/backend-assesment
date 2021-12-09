from locale import currency
from ..models import Agent, Airline, Itinerary, Leg

def create_legs(legs):
    db_legs = []
    for leg in legs:
        try:
            Leg.objects.get(api_id = leg['id'])
        except Leg.DoesNotExist:
            try:
                airline = Airline.objects.get(airline_id = leg['airline_id'], name = leg['airline_name'])
            except Airline.DoesNotExist:
                airline = Airline(airline_id = leg['airline_id'], name = leg['airline_name'] )
                airline.save()
            db_leg = Leg(
                api_id=leg['id'],
                departure_airport = leg['departure_airport'],
                departure_time = leg['departure_time'], 
                arrival_airport = leg['arrival_airport'],
                arrival_time = leg['arrival_time'], 
                stops = int(leg['stops']),
                duration_mins = int(leg['duration_mins']),
                airline = airline
            )
            db_legs.append(db_leg)
    Leg.objects.bulk_create(db_legs)


def create_itineraries(itineraries):
    for itinerary in itineraries:
        try:
            Itinerary.objects.get(api_id = itinerary["id"])
        except Itinerary.DoesNotExist:
            try:
                agent = Agent.objects.get(name = itinerary['agent'])
            except Agent.DoesNotExist:
                agent = Agent(name = itinerary['agent'], rating = itinerary["agent_rating"] )
                agent.save()
            db_legs = Leg.objects.filter(api_id__in = itinerary['legs'])
            currency_price = itinerary['price']     
            currency = currency_price[:1] if currency_price[1].isdigit() else ''.join(map(lambda char: '' if char.isdigit() else char, currency_price))
            currency = currency.replace(' ', '')
            price = float(''.join(map(lambda char: char if char.isdigit() else '', currency_price)))
            db_itinerary = Itinerary(
                api_id = itinerary['id'],
                price = price,
                currency = currency,
                agent = agent
            )
            db_itinerary.save()
            db_itinerary.legs.add(db_legs)

