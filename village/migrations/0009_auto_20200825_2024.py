# Generated by Django 3.0.6 on 2020-08-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0008_auto_20200825_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='document',
            field=models.FileField(blank='True', default='', null='True', upload_to='documentation/'),
        ),
    ]
