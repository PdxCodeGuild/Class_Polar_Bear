# Generated by Django 3.2.8 on 2021-12-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211229_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userandpassword',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userandpassword',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
