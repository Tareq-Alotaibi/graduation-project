# Generated by Django 4.1.2 on 2022-10-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='total_cars',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]