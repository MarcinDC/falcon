# Generated by Django 2.1.2 on 2018-11-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CracowDB', '0002_auto_20181119_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='kwdata',
            name='date_of_close',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kwdata',
            name='date_of_save',
            field=models.DateField(blank=True, null=True),
        ),
    ]
