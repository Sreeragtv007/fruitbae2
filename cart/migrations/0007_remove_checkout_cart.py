# Generated by Django 4.2 on 2024-03-25 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_checkout_cart_checkout_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='cart',
        ),
    ]
