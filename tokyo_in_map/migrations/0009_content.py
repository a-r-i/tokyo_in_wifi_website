# Generated by Django 2.1.5 on 2019-01-14 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokyo_in_map', '0008_auto_20181210_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_url', models.CharField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tokyo_in_map.Spot')),
            ],
        ),
    ]
