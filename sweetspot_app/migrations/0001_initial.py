# Generated by Django 5.0.4 on 2024-04-17 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank='True', null=True, upload_to='cakes/')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomizeOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cakeId', models.IntegerField()),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=1, null=True)),
                ('flavor', models.CharField(blank=True, choices=[('Vanilla', 'Vanilla'), ('Chocolate', 'Chocolate'), ('Strawberry', 'Strawberry')], default='Vanilla', max_length=100, null=True)),
                ('toppings', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('mobileNo', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=8)),
                ('isActive', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.cake')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.cart')),
                ('customization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sweetspot_app.customizeoption')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.cake')),
                ('customization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.customizeoption')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.user'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweetspot_app.user'),
        ),
    ]
