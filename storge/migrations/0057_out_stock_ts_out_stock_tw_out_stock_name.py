# Generated by Django 4.1.4 on 2023-04-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0056_out_stock_iteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='out_stock',
            name='TS',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='الشيت الكلي'),
        ),
        migrations.AddField(
            model_name='out_stock',
            name='TW',
            field=models.FloatField(blank=True, default=0, max_length=100, null=True, verbose_name='الوزن الكلي'),
        ),
        migrations.AddField(
            model_name='out_stock',
            name='name',
            field=models.CharField(default='اذن صرف', max_length=100, verbose_name='الاسم'),
        ),
    ]
