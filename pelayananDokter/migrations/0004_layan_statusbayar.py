# Generated by Django 4.1 on 2022-10-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelayananDokter', '0003_alter_layan_statusobat'),
    ]

    operations = [
        migrations.AddField(
            model_name='layan',
            name='statusBayar',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
