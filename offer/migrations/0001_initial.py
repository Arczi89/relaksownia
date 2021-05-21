# Generated by Django 3.2 on 2021-05-21 21:58

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfferConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', djrichtextfield.models.RichTextField(default='', verbose_name='Text wyswietlany na gorze strony pod menu')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
            ],
            options={
                'verbose_name': 'Oferta - konfiguracja',
                'verbose_name_plural': 'Oferta - konfiguracja',
            },
        ),
        migrations.CreateModel(
            name='OfferItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Tytul')),
                ('text', djrichtextfield.models.RichTextField(verbose_name='Tresc')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Obrazek')),
                ('image_alt', models.TextField(verbose_name='Nazwa')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
                ('element_order', models.IntegerField(default=0, verbose_name='Kolejnosc')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Lista ofert',
            },
        ),
    ]
