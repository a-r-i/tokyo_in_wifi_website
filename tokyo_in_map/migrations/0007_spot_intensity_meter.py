# Generated by Django 2.1.1 on 2018-12-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokyo_in_map', '0006_spot_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='intensity_meter',
            field=models.IntegerField(null=True),
        ),
    ]
