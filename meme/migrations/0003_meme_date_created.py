# Generated by Django 3.1.2 on 2021-02-11 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0002_auto_20210210_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]