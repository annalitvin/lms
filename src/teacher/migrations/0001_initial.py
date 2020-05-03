# Generated by Django 3.0.5 on 2020-05-01 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=100)),
                ('employment_date', models.DateField(default=datetime.date(2020, 5, 1))),
            ],
        ),
    ]
