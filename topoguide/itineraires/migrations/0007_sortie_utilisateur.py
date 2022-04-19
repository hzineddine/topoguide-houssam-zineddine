# Generated by Django 4.0.4 on 2022-04-17 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itineraires', '0006_meteo_sortie_difficulte_ressentie_sortie_meteo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sortie',
            name='utilisateur',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]