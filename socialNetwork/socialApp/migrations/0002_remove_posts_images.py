# Generated by Django 4.0.2 on 2022-03-24 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='images',
        ),
    ]
