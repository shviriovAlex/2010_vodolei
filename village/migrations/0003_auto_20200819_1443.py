# Generated by Django 3.0.6 on 2020-08-19 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0002_целевые_членские_электроэнергия'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Целевые',
        ),
        migrations.DeleteModel(
            name='Членские',
        ),
        migrations.DeleteModel(
            name='Электроэнергия',
        ),
    ]
