# Generated by Django 4.0 on 2021-12-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='currency',
            field=models.CharField(default='', max_length=6, verbose_name='Moneda'),
            preserve_default=False,
        ),
    ]
