# Generated by Django 3.0.6 on 2020-08-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0011_auto_20200825_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruleinside',
            name='document',
            field=models.FileField(blank='True', default='', null='True', upload_to='documentation/'),
        ),
        migrations.AlterField(
            model_name='протоколы_собраний',
            name='document',
            field=models.FileField(blank='True', default='', null='True', upload_to='media'),
        ),
    ]
