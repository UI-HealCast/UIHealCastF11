# Generated by Django 4.1 on 2022-10-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_alter_landing_is_admin_alter_landing_is_apotek_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landing',
            name='username',
            field=models.CharField(default='-', max_length=30),
            preserve_default=False,
        ),
    ]
