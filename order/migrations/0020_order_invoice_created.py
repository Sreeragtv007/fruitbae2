# Generated by Django 4.2 on 2024-04-28 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_order_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_created',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]