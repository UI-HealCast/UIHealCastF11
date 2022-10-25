# Generated by Django 4.1 on 2022-10-25 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing', '0002_landing_is_admin_landing_is_apotek_landing_is_doctor_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Layan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keluhan', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=60)),
                ('tanggal_janji', models.DateTimeField()),
                ('noHP', models.CharField(max_length=12)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('dokter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.landing')),
            ],
        ),
    ]
