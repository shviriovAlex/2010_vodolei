# Generated by Django 3.0.6 on 2020-10-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0016_auto_20200911_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='главная',
            name='document_2',
            field=models.FileField(blank='True', null='True', upload_to='media_community/', verbose_name='Файл'),
            preserve_default='True',
        ),
    ]
