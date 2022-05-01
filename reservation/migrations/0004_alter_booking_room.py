# Generated by Django 4.0.4 on 2022-05-01 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_booking_create_date_hotel_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='reservation.room'),
        ),
    ]
