# Generated by Django 3.0.6 on 2020-08-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0009_auto_20200825_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='протоколы_собраний',
            name='document',
            field=models.FileField(blank='True', default='', null='True', upload_to='media/'),
        ),
    ]