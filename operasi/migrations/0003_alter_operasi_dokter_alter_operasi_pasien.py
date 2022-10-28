# Generated by Django 4.1 on 2022-10-27 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_landing_username'),
        ('operasi', '0002_alter_operasi_dokter_alter_operasi_pasien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operasi',
            name='dokter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dokter_operasi', to='landing.landing'),
        ),
        migrations.AlterField(
            model_name='operasi',
            name='pasien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasien_operasi', to='landing.landing'),
        ),
    ]