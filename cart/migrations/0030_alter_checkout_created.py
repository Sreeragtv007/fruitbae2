# Generated by Django 4.2 on 2024-04-09 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0029_alter_checkout_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 9, 10, 48, 1, 857452)),
        ),
    ]