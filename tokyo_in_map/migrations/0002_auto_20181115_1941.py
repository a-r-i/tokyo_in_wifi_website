# Generated by Django 2.1.1 on 2018-11-15 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tokyo_in_map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='voice',
            old_name='path',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='point',
            name='voice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='voice', to='tokyo_in_map.Voice'),
        ),
        migrations.AddField(
            model_name='point',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movie', to='tokyo_in_map.Movie'),
        ),
    ]
