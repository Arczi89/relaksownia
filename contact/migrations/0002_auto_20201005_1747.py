# Generated by Django 3.1.2 on 2020-10-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
