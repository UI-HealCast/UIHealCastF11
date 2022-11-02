# Generated by Django 4.1 on 2022-10-31 10:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_landing_username'),
        ('pembayaran', '0003_alter_bayar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bayar',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bayar',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='landing_user', to='landing.landing'),
        ),
    ]
