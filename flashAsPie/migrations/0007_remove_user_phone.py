# Generated by Django 3.0.8 on 2020-07-10 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashAsPie', '0006_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]