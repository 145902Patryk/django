# Generated by Django 2.0.13 on 2020-01-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szkolenia', '0013_auto_20200116_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='szkolenia',
            name='opic',
            field=models.TextField(blank=True),
        ),
    ]
