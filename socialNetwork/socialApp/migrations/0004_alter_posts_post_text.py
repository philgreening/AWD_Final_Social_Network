# Generated by Django 4.0.2 on 2022-02-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0003_userprofile_followers_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_text',
            field=models.CharField(max_length=250),
        ),
    ]
