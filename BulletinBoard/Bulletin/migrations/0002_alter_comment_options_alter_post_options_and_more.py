# Generated by Django 4.0.1 on 2022-01-25 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bulletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарий'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
    ]
