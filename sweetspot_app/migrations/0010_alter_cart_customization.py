# Generated by Django 5.0.4 on 2024-04-26 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetspot_app', '0009_alter_cart_customization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.cakecustomization'),
        ),
    ]