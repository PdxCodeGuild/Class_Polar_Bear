# Generated by Django 3.2.8 on 2022-01-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('height', models.FloatField(default=3)),
                ('weight', models.FloatField(default=50)),
                ('image_front', models.CharField(max_length=200)),
                ('image_back', models.CharField(max_length=200)),
                ('types', models.CharField(max_length=200)),
            ],
        ),
    ]