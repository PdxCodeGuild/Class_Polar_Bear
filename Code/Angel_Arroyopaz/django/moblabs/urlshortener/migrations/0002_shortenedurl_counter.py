# Generated by Django 3.2.8 on 2021-11-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurl',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
