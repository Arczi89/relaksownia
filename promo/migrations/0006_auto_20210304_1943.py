# Generated by Django 3.1.5 on 2021-03-04 18:43

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0005_auto_20210304_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promoconfiguration',
            options={'verbose_name': 'Konfiguracja promocji', 'verbose_name_plural': 'Konfiguracja promocji'},
        ),
        migrations.AlterModelOptions(
            name='promoemailconfiguration',
            options={'verbose_name': 'Konfiguracja wysylki', 'verbose_name_plural': 'Konfiguracja wysylki'},
        ),
        migrations.AlterField(
            model_name='promoemailconfiguration',
            name='from_email',
            field=models.CharField(default='zamowienia@relaksownia.org.pl', max_length=100, verbose_name='Od kogo?'),
        ),
        migrations.AlterField(
            model_name='promoemailconfiguration',
            name='message',
            field=djrichtextfield.models.RichTextField(default='Dziękuję za zainteresowanie książką Doskonale Niedoskonali i złożenie zamówienia. Twoje zamówienie zostało przyjęte i zostanie realizowane jak tylko płatność zostanie potwierdzona. W dniu wysyłki zostaniesz o tym poinformowany drogą mailową i otrzymasz informacje zawierające:\n                    <ul>\n                        <li>numer listu przewozowego</li>\n                        <li>link do strony firmy kurierskiej umożliwiający monitorowanie przesyłki</li>\n                        <li>instrukcję postępowania podczas odbioru przesyłki od kuriera</li>\n                    </ul>\n                    Serdecznie pozdrawiam, Justyna', verbose_name='Tresc wiadomosci'),
        ),
    ]