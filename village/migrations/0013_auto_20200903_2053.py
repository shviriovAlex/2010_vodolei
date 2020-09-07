# Generated by Django 3.0.6 on 2020-09-03 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0012_auto_20200825_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Главная',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='', max_length=250)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank='True', null='True', upload_to='media_community/', verbose_name='Изображение')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameModel(
            old_name='Leadership',
            new_name='Администрация',
        ),
        migrations.DeleteModel(
            name='ForCommunity',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
        migrations.DeleteModel(
            name='RuleInside',
        ),
        migrations.RenameField(
            model_name='целевые',
            old_name='publish',
            new_name='опубликовано',
        ),
        migrations.RenameField(
            model_name='членские',
            old_name='publish',
            new_name='опубликовано',
        ),
        migrations.RenameField(
            model_name='электроэнергия',
            old_name='publish',
            new_name='опубликовано',
        ),
    ]
