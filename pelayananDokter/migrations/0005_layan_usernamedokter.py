# Generated by Django 4.1 on 2022-10-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelayananDokter', '0004_layan_statusbayar'),
    ]

    operations = [
        migrations.AddField(
            model_name='layan',
            name='usernameDokter',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
