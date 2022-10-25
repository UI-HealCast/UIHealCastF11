# Generated by Django 4.1 on 2022-10-25 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_landing_username'),
        ('pelayananDokter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layan',
            name='dokter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dokter', to='landing.landing'),
        ),
        migrations.AlterField(
            model_name='layan',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pasien', to='landing.landing'),
        ),
    ]
