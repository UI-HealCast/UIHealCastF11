# Generated by Django 4.1 on 2022-10-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_alter_landing_doctorready'),
    ]

    operations = [
        migrations.AddField(
            model_name='landing',
            name='username',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
