# Generated by Django 3.0.5 on 2020-05-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20200509_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
