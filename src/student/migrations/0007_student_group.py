# Generated by Django 3.0.5 on 2020-05-11 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20200509_1416'),
        ('student', '0006_student_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='group.Group'),
        ),
    ]
