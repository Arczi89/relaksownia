# Generated by Django 3.1.2 on 2020-12-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='photo_alt',
            field=models.CharField(max_length=200),
        ),
    ]
