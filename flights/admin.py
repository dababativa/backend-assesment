from django.contrib import admin, messages
from django.http import response

from .models import Airline, Agent, Leg, Itinerary
from .utils import get_flight_information_utils
from .functions.itinerary_functions import create_itineraries, create_legs


# Display
@admin.display(description='Price')
def full_price(obj):
    return f'{obj.currency}{obj.price}'

# Admin Models
class ItineraryAdmin(admin.ModelAdmin):
    actions=['get_flights_information']
    filter_horizontal = ('legs',)
    list_display = ['api_id', full_price, 'agent']
    autocomplete_fields = ['agent']
    # Actions
    @admin.action(description='Actualizar información')
    def get_flights_information(self, request, queryset):
        flights = get_flight_information_utils()
        itineraries = flights['itineraries']
        legs = flights['legs']
        create_legs(legs)
        create_itineraries(itineraries)

        self.message_user(request, "Successfully created itineraries", messages.SUCCESS)


class AgentAdmin(admin.ModelAdmin):
    search_fields = ['name']
class AirlineAdmin(admin.ModelAdmin):
    search_fields = ['name', 'airline_id']
class LegAdmin(admin.ModelAdmin):
    list_display = ['departure_airport', 'departure_time', 'arrival_airport', 'arrival_time', 'airline']
    search_fields = ['departure_airport', 'arrival_airport', 'airline__name', 'airline__airline_id']
    autocomplete_fields = ['airline']
    

# Register your models here.
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Leg, LegAdmin)

