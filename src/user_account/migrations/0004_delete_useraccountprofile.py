# Generated by Django 3.0.5 on 2020-06-13 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_auto_20200613_1124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccountProfile',
        ),
    ]
