# Generated by Django 2.1.2 on 2018-11-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CracowDB', '0004_auto_20181119_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kwdata',
            name='kw_number',
            field=models.CharField(default='', help_text='pełny numer kw', max_length=15),
        ),
    ]
