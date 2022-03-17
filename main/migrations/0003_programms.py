# Generated by Django 3.2.7 on 2022-03-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_news_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250, verbose_name='Название программы')),
                ('date', models.DateField(verbose_name='Начало')),
                ('length', models.CharField(max_length=155, verbose_name='Длительность')),
                ('location', models.CharField(max_length=150, verbose_name='Местоположение')),
                ('set', models.CharField(choices=[('ОТКРЫТ', 'открыт'), ('ЗАКРЫТ', 'закрыт')], default='ЗАКРЫТ', max_length=50, verbose_name='Набор')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
    ]
