# Generated by Django 3.2.7 on 2022-05-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_consulting_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
