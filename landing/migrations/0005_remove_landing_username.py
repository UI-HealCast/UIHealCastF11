# Generated by Django 4.1 on 2022-10-25 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_landing_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landing',
            name='username',
        ),
    ]