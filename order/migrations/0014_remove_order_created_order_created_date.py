# Generated by Django 4.2 on 2024-04-20 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_order_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
