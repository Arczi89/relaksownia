# Generated by Django 3.1.1 on 2020-09-27 13:06

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_text', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='images/')),
                ('image_alt', models.CharField(max_length=400)),
                ('description', djrichtextfield.models.RichTextField()),
                ('visible', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('photo_alt', models.CharField(max_length=400)),
                ('description', djrichtextfield.models.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_alt', models.CharField(max_length=400)),
                ('visible', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
