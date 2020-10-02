# Generated by Django 3.1.2 on 2020-10-02 20:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
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
                ('main_title', models.TextField()),
                ('main_text', djrichtextfield.models.RichTextField()),
                ('update_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='OfferItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', djrichtextfield.models.RichTextField()),
                ('image', models.ImageField(upload_to='')),
                ('image_alt', models.TextField()),
                ('update_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('conf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.offerconfiguration')),
            ],
        ),
    ]
