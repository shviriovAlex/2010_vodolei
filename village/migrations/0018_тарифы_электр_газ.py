# Generated by Django 3.0.6 on 2020-10-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0017_главная_document_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Тарифы_Электр_Газ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('дата_от', models.CharField(max_length=250)),
                ('электроэнергия', models.CharField(max_length=250)),
                ('газ', models.CharField(max_length=250)),
                ('прежний_электроэнергия', models.CharField(max_length=250)),
                ('прежний_газ', models.CharField(max_length=250)),
            ],
        ),
    ]
