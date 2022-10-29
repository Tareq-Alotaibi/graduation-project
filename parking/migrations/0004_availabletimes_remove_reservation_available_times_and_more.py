# Generated by Django 4.1.2 on 2022-10-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_reservation_car_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_times', models.CharField(choices=[('Time1', '09:00 – 10:00'), ('Time2', '10:00 – 11:00'), ('Time3', '11:00 – 12:00'), ('Time4', '12:00 – 13:00'), ('Time5', '13:00 – 14:00'), ('Time6', '14:00 – 15:00'), ('Time7', '15:00 – 16:00'), ('Time8', '16:00 – 17:00')], max_length=250, verbose_name='Available Times')),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='available_times',
        ),
        migrations.AddField(
            model_name='reservation',
            name='available_times',
            field=models.ManyToManyField(to='parking.availabletimes'),
        ),
    ]
