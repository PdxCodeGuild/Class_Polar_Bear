# Generated by Django 3.2.8 on 2021-11-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
