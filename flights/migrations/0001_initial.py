# Generated by Django 4.0 on 2021-12-09 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('rating', models.FloatField(verbose_name='Puntaje')),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_id', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=128)),
                ('departure_airport', models.CharField(max_length=128, verbose_name='Aeropuerto de salida')),
                ('arrival_airport', models.CharField(max_length=128, verbose_name='Aeropuerto de llegada')),
                ('departure_time', models.DateTimeField(verbose_name='Hora de salida')),
                ('arrival_time', models.DateTimeField(verbose_name='Hora de llegada')),
                ('stops', models.PositiveIntegerField(verbose_name='Cantidad de paradas')),
                ('duration_mins', models.PositiveIntegerField(verbose_name='Duración en minutos')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='flights.airline')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=128)),
                ('price', models.FloatField(verbose_name='Precio')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='flights.agent')),
                ('legs', models.ManyToManyField(to='flights.Leg')),
            ],
        ),
    ]
