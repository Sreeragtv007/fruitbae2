# Generated by Django 4.2 on 2024-03-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_remove_cart_product_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_complted',
            field=models.BooleanField(default=False),
        ),
    ]
