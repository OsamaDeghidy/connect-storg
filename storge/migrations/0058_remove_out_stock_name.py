# Generated by Django 4.1.4 on 2023-04-06 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0057_out_stock_ts_out_stock_tw_out_stock_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='out_stock',
            name='name',
        ),
    ]