# Generated by Django 4.0.6 on 2022-07-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField()),
                ('station_id', models.IntegerField()),
                ('name_finnish', models.CharField(max_length=50)),
                ('name_swidish', models.CharField(max_length=50)),
                ('name_english', models.CharField(max_length=50)),
                ('address_finnish', models.CharField(max_length=50)),
                ('address_swedish', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('city_swedish', models.CharField(max_length=50)),
                ('operator', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('coodinate_x', models.FloatField()),
                ('coodinate_y', models.FloatField()),
            ],
        ),
    ]
