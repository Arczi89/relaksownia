# Generated by Django 3.2 on 2021-04-16 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0007_auto_20210416_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoemailconfiguration',
            name='admin_email',
            field=models.CharField(default='zamowienia@relaksownia.org.pl', max_length=100, verbose_name='Twój email'),
        ),
    ]
