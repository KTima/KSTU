# Generated by Django 3.2.7 on 2022-03-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение статьи'),
        ),
    ]
