# Generated by Django 4.1.4 on 2023-02-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0013_linght_width_rename_width_pukker_total_linght_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='out_stock',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]