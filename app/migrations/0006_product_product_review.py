# Generated by Django 4.2 on 2024-03-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
