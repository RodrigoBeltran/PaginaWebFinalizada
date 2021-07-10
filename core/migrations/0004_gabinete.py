# Generated by Django 3.2.5 on 2021-07-09 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_juegos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gabinete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('formato', models.CharField(max_length=70)),
                ('fuentePoder', models.CharField(max_length=70)),
                ('ubicacion', models.CharField(max_length=70)),
                ('panel', models.CharField(max_length=70)),
                ('ventiladores', models.CharField(max_length=70)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='gabinetes')),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.distribuidor')),
            ],
        ),
    ]
