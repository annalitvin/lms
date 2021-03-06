# Generated by Django 3.0.5 on 2020-05-03 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('specialty', models.CharField(max_length=40, unique=True)),
                ('course_name', models.CharField(max_length=80)),
                ('number_persons', models.PositiveSmallIntegerField()),
                ('type', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], max_length=8)),
                ('is_paid', models.BooleanField()),
                ('date_start', models.DateField()),
            ],
        ),
    ]
