# Generated by Django 4.1.1 on 2022-10-27 10:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing', '0008_landing_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keluhan', models.CharField(max_length=300)),
                ('tanggal_janji', models.DateTimeField(default=datetime.datetime.now)),
                ('noHP', models.CharField(max_length=12)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('username', models.CharField(default='-', max_length=30)),
                ('hasilPeriksa', models.CharField(default='-', max_length=150)),
                ('dokter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dokter', to='landing.landing')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pasien', to='landing.landing')),
            ],
        ),
    ]
