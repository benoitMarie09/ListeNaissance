# Generated by Django 4.1.7 on 2023-02-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_cadeau'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]
