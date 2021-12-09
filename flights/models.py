from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length= 128, verbose_name='Nombre')
    rating = models.FloatField(verbose_name='Puntaje')
    
    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Airline(models.Model):
    airline_id = models.CharField(max_length= 128)
    name = models.CharField(max_length= 128,verbose_name='Nombre')
    def __str__(self):
        return f'{self.airline_id} - {self.name}'

class Leg(models.Model):
    api_id = models.CharField(max_length= 128)
    departure_airport = models.ForeignKey(Airport, on_delete=models.RESTRICT, related_name='departure_leg', verbose_name='Aeropuerto de salida')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.RESTRICT, related_name='arrival_leg', verbose_name='Aeropuerto de llegada')
    departure_time = models.DateTimeField(verbose_name='Hora de salida')
    arrival_time = models.DateTimeField(verbose_name='Hora de llegada')
    stops = models.PositiveIntegerField(verbose_name='Cantidad de paradas')
    duration_mins = models.PositiveIntegerField(verbose_name='Duración en minutos')
    airline = models.ForeignKey(Airline, on_delete=models.RESTRICT, verbose_name='Aerolinea')
    
    def __str__(self):
        return f'{self.departure_airport} - {self.arrival_airport} ({self.airline.name})'

class Itinerary(models.Model):
    api_id = models.CharField(max_length= 128)
    price = models.FloatField(verbose_name='Precio', validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=7, verbose_name='Moneda')
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT, verbose_name = 'Agente')
    legs = models.ManyToManyField(Leg)
    
    def __str__(self):
        return f'{self.id} - {self.agent}'

    class Meta:
        verbose_name_plural: 'itineraries'

