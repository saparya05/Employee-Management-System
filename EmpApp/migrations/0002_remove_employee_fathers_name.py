# Generated by Django 5.0.2 on 2024-07-13 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='fathers_name',
        ),
    ]
