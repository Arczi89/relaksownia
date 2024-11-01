# Generated by Django 3.2 on 2021-05-21 21:58

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
                ('main_image', models.ImageField(upload_to='images/', verbose_name='Glowny obrazek')),
                ('main_image_alt', models.CharField(max_length=200, verbose_name='Nazwa')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
            ],
            options={
                'verbose_name': 'Konfiguracja pytan',
                'verbose_name_plural': 'Konfiguracja pytan',
            },
        ),
        migrations.CreateModel(
            name='FaqItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', djrichtextfield.models.RichTextField(verbose_name='Tresc pytania')),
                ('answer_text', djrichtextfield.models.RichTextField(verbose_name='Tresc odpowiedzi')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
                ('element_order', models.IntegerField(default=0, verbose_name='Kolejnosc')),
            ],
            options={
                'verbose_name': 'Pytanie i odpowiedz (faq)',
                'verbose_name_plural': 'Pytania i odpowiedzi (faqs)',
            },
        ),
    ]
