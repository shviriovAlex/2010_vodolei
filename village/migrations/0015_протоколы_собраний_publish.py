# Generated by Django 3.0.6 on 2020-09-09 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0014_auto_20200903_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='протоколы_собраний',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
