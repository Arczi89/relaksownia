# Generated by Django 3.1.2 on 2020-10-17 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201018_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 1, 19, 27, 687226), help_text='Data publikacji posta'),
        ),
    ]