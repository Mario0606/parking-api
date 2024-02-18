# Generated by Django 4.2.9 on 2024-02-18 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'ParkingLot',
                'verbose_name_plural': 'ParkingLots',
                'db_table': 'parking_lots',
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('paid_at', models.DateTimeField(null=True)),
                ('left_at', models.DateTimeField(null=True)),
                ('parking_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking', to='parking.parkinglot')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking', to='control.vehicle')),
            ],
            options={
                'verbose_name': 'Parking',
                'verbose_name_plural': 'Parkings',
                'db_table': 'parkings',
            },
        ),
    ]
