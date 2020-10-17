# Generated by Django 3.1.2 on 2020-10-17 13:26

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionTreeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', djrichtextfield.models.RichTextField(help_text='Tekst wyswietlany w drzewku na podstronie opinii')),
                ('img', djrichtextfield.models.RichTextField(help_text='Ilustracja wyswietlana w drzewku na podstronie opinii')),
            ],
        ),
    ]
