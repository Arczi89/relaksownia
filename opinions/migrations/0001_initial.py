# Generated by Django 3.2 on 2021-05-21 21:58

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion_text', djrichtextfield.models.RichTextField(verbose_name='Tekst rekomendacji')),
                ('customer_name', models.CharField(max_length=400, verbose_name='Imie osoby polecajacej')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
                ('element_order', models.IntegerField(default=0, verbose_name='Kolejnosc')),
            ],
            options={
                'verbose_name': 'Opinia',
                'verbose_name_plural': 'Opinie',
            },
        ),
        migrations.CreateModel(
            name='OpinionsConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='images/', verbose_name='Obrazek wyswietlany na gorze strony pod menu')),
                ('main_image_alt', models.CharField(max_length=200, verbose_name='Nazwa')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
                ('tree_img', models.ImageField(upload_to='images/', verbose_name='Obrazek wyswietlany jako glowny w drzewku')),
                ('tree_header', models.TextField(default='Dlaczego nasza oferta jest taka wyjątkowa?', verbose_name='Tekst nad drzewkiem')),
            ],
            options={
                'verbose_name': 'Konfiguracja opinii',
                'verbose_name_plural': 'Konfiguracja opinii',
            },
        ),
        migrations.CreateModel(
            name='OpinionTreeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', djrichtextfield.models.RichTextField(verbose_name='Tekst wyswietlany w drzewku na podstronie opinii')),
                ('img', models.ImageField(upload_to='images/', verbose_name='Ilustracja wyswietlana w drzewku na podstronie opinii')),
                ('element_order', models.IntegerField(default=0, verbose_name='Kolejnosc')),
            ],
            options={
                'verbose_name': 'Element drzewka na stronie opinii',
                'verbose_name_plural': 'Elementy drzewka na stronie opinie',
            },
        ),
    ]
