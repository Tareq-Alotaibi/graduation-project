# Generated by Django 4.1.2 on 2022-10-29 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0008_alter_reservation_parking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AvailableTimes',
        ),
    ]