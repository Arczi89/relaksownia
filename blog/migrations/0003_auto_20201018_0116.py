# Generated by Django 3.1.2 on 2020-10-17 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201018_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 1, 16, 27, 716777), help_text='Data publikacji posta'),
        ),
    ]