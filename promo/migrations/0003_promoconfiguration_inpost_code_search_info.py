# Generated by Django 3.1.5 on 2021-03-02 21:06

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0002_auto_20210301_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoconfiguration',
            name='inpost_code_search_info',
            field=djrichtextfield.models.RichTextField(default='https://inpost.pl/znajdz-paczkomat', verbose_name='Link do wyszukiwarki paczkomatow INPOST'),
        ),
    ]