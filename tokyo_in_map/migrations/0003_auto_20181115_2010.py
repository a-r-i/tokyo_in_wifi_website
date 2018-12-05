# Generated by Django 2.1.1 on 2018-11-15 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('tokyo_in_map', '0002_auto_20181115_1941'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voice',
            new_name='Content',
        ),
        migrations.RemoveField(
            model_name='point',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='point',
            name='voice',
        ),
        migrations.AddField(
            model_name='point',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tokyo_in_map.Content'),
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
