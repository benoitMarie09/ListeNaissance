# Generated by Django 4.1.7 on 2023-02-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liste', '0002_cadeau_est_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeau',
            name='montant_reserve',
            field=models.FloatField(default=0),
        ),
    ]
