# Generated by Django 4.1.2 on 2022-11-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0009_delete_availabletimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='parking',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]