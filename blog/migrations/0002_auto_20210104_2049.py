# Generated by Django 3.1.2 on 2021-01-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publication_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Data publikacji posta'),
        ),
    ]