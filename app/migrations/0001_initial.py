# Generated by Django 5.0.6 on 2024-07-04 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('category_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=100)),
                ('pprice', models.IntegerField()),
                ('pdate', models.DateField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
    ]
