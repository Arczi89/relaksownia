# Generated by Django 3.2 on 2021-04-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0006_auto_20210304_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promoemailconfiguration',
            name='message',
        ),
        migrations.RemoveField(
            model_name='promoemailconfiguration',
            name='subject',
        ),
        migrations.AlterField(
            model_name='promoclient',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nazwa firmy oraz adres'),
        ),
    ]