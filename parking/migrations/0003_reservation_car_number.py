# Generated by Django 4.1.2 on 2022-10-29 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_alter_parking_total_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='car_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]