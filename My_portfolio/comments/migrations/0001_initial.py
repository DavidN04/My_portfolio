# Generated by Django 4.0.5 on 2022-06-22 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Имя автора', max_length=255, verbose_name='Имя автора')),
                ('text', models.TextField(help_text='Текст комментария', verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(help_text='Проект', on_delete=django.db.models.deletion.CASCADE, to='mainapp.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('created',),
            },
        ),
    ]
