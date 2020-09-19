# Generated by Django 3.1.1 on 2020-09-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=3000)),
                ('answer_text', models.CharField(max_length=3000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
