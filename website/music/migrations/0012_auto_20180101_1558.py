# Generated by Django 2.0 on 2018-01-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_remove_album_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
