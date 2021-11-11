# Generated by Django 3.2.8 on 2021-11-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_item', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Incomplete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incomplete_item', models.CharField(max_length=200)),
            ],
        ),
    ]
