# Generated by Django 4.1.4 on 2022-12-29 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gram_Categore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='In_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quntity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Iteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('quntity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=100)),
                ('degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.degree')),
                ('gram_categore', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.gram_categore')),
            ],
        ),
        migrations.CreateModel(
            name='Main_categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Peper_type_country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('main_categorey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.main_categorey')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('linght', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('grams', models.IntegerField(default=0)),
                ('weaight', models.IntegerField(default=0)),
                ('sheet', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=100)),
                ('iteam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.iteam')),
            ],
        ),
        migrations.CreateModel(
            name='Pukker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('width', models.IntegerField(default=0)),
                ('weaight', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=100)),
                ('iteam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.iteam')),
            ],
        ),
        migrations.CreateModel(
            name='Pako',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('linght', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('grams', models.IntegerField(default=0)),
                ('weaight', models.IntegerField(default=0)),
                ('sheet', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=100)),
                ('iteam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.iteam')),
            ],
        ),
        migrations.CreateModel(
            name='Out_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quntity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('In_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.in_stock')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.customer')),
                ('iteam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.iteam')),
            ],
        ),
        migrations.AddField(
            model_name='iteam',
            name='main_categorey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.main_categorey'),
        ),
        migrations.AddField(
            model_name='iteam',
            name='peper_type_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.peper_type_country'),
        ),
        migrations.AddField(
            model_name='iteam',
            name='sub_categorey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.sub_categorey'),
        ),
        migrations.AddField(
            model_name='in_stock',
            name='iteam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.iteam'),
        ),
        migrations.AddField(
            model_name='in_stock',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storge.supplier'),
        ),
    ]