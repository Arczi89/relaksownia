# Generated by Django 3.1.1 on 2020-09-19 20:47

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containeritem',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='containeritem',
            name='header_text',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='containeritem',
            name='image_alternate_text',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='info',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='photo_alternate_text',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='image_alternate_text',
            field=models.CharField(max_length=400),
        ),
    ]
