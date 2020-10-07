# Generated by Django 3.1.2 on 2020-10-07 16:14

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', djrichtextfield.models.RichTextField()),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=400)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
    ]
