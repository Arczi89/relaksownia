# Generated by Django 3.1.2 on 2020-11-23 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201123_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 21, 31, 45, 661104), help_text='Data publikacji posta'),
        ),
    ]
