# Generated by Django 3.2.8 on 2022-01-12 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valuechain', '0005_auto_20220111_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='manufacturer',
        ),
    ]
