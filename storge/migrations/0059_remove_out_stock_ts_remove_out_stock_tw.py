# Generated by Django 4.1.4 on 2023-04-13 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0058_remove_out_stock_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='out_stock',
            name='TS',
        ),
        migrations.RemoveField(
            model_name='out_stock',
            name='TW',
        ),
    ]