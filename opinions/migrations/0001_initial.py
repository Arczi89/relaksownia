# Generated by Django 3.1.2 on 2020-10-17 23:16

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion_text', djrichtextfield.models.RichTextField(help_text='Tekst rekomendacji')),
                ('customer_name', models.CharField(help_text='Imie osoby polecajacej', max_length=400)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
            ],
        ),
        migrations.CreateModel(
            name='OpinionsConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(help_text='Obrazek wyswietlany na gorze strony pod menu', upload_to='images/')),
                ('main_image_alt', models.CharField(help_text='Tekst wyswietlany w przypadku gdyby obrazek sie nie zaladowal', max_length=400)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
                ('tree_img', models.ImageField(help_text='Obrazek wyswietlany jako głowny w drzewku', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='OpinionTreeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', djrichtextfield.models.RichTextField(help_text='Tekst wyswietlany w drzewku na podstronie opinii')),
                ('img', models.ImageField(help_text='Ilustracja wyswietlana w drzewku na podstronie opinii', upload_to='images/')),
            ],
        ),
    ]