# Generated by Django 3.2.7 on 2022-05-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220517_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulting',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время'),
        ),
    ]