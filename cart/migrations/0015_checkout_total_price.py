# Generated by Django 4.2 on 2024-03-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_remove_checkout_cart_checkout_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]