# Generated by Django 2.0.13 on 2020-01-16 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('szkolenia', '0012_auto_20200116_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizatorzy',
            name='stworzony_przez',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
