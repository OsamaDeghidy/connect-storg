# Generated by Django 3.2.5 on 2023-06-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0059_remove_out_stock_ts_remove_out_stock_tw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gram_categore',
            name='code',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='gram_categore',
            name='name',
            field=models.FloatField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='width',
            name='code',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='width',
            name='name',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
