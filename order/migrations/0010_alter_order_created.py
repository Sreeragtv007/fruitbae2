# Generated by Django 4.2 on 2024-04-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
