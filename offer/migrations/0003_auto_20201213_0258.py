# Generated by Django 3.1.2 on 2020-12-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20201123_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='offeritem',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='offerconfiguration',
            name='main_image_alt',
            field=models.CharField(help_text='Tekst wyświetlany w przypadku gdyby obrazek sie nie zaladowal', max_length=200),
        ),
    ]
