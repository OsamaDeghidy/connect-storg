# Generated by Django 4.1.4 on 2023-02-06 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0014_alter_out_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pako',
            name='iteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.iteam'),
        ),
        migrations.AlterField(
            model_name='pukker',
            name='iteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.iteam'),
        ),
        migrations.AlterField(
            model_name='sub',
            name='iteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.iteam'),
        ),
    ]