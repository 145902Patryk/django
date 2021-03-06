# Generated by Django 2.2.6 on 2019-11-22 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('szkolenia', '0005_organizatorzy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Szkolenia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('adres', models.CharField(max_length=70)),
                ('cena', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('opic', models.FileField(upload_to='')),
                ('idOrganizatora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkolenia.Organizatorzy')),
            ],
        ),
    ]
