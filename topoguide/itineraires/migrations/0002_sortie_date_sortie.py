# Generated by Django 4.0.3 on 2022-04-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sortie',
            name='data_sortie',
            field=models.DateField(default=0, verbose_name='Date de sortie'),
            preserve_default=False,
        ),
    ]
