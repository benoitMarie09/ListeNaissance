# Generated by Django 4.1.7 on 2023-02-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liste', '0004_remove_cadeau_est_reserve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadeau',
            name='montant_reserve',
        ),
        migrations.AddField(
            model_name='cadeau',
            name='montant_restant',
            field=models.FloatField(default=0),
        ),
    ]
