# Generated by Django 5.0.4 on 2024-04-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetspot_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='isActive',
        ),
        migrations.AlterField(
            model_name='user',
            name='mobileNo',
            field=models.CharField(),
        ),
    ]
