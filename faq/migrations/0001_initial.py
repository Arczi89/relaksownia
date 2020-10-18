# Generated by Django 3.1.2 on 2020-10-17 23:16

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(help_text='Obrazek wyswietlany na gorze strony pod menu', upload_to='images/')),
                ('main_image_alt', models.CharField(help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal', max_length=400)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
            ],
        ),
        migrations.CreateModel(
            name='FaqItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', djrichtextfield.models.RichTextField()),
                ('answer_text', djrichtextfield.models.RichTextField()),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
            ],
        ),
    ]
