# Generated by Django 4.0.5 on 2022-06-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=True, help_text='Опубликовать проект?', verbose_name='Статус проекта'),
        ),
    ]