# Generated by Django 3.2.8 on 2021-12-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_userandpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userandpassword',
            name='user',
        ),
        migrations.AddField(
            model_name='userandpassword',
            name='username',
            field=models.CharField(default='james', max_length=200),
        ),
        migrations.AlterField(
            model_name='userandpassword',
            name='password',
            field=models.CharField(default='password', max_length=200),
        ),
    ]
