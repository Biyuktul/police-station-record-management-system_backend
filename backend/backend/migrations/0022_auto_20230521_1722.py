# Generated by Django 2.1.15 on 2023-05-21 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20230521_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='victims',
            name='FIR_ID',
        ),
        migrations.RemoveField(
            model_name='witness',
            name='FIR_ID',
        ),
    ]
