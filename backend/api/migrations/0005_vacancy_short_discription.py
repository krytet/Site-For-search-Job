# Generated by Django 3.2.9 on 2022-02-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_vacancy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='short_discription',
            field=models.CharField(blank=True, max_length=255, verbose_name='Короткое описание'),
        ),
    ]
