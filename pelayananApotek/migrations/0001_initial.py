# Generated by Django 4.1 on 2022-10-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_obat', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
                ('kuantitas', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
