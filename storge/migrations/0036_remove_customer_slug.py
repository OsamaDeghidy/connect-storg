# Generated by Django 4.1.4 on 2023-02-11 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0035_alter_customer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
    ]