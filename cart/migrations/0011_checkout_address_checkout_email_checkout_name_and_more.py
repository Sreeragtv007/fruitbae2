# Generated by Django 4.2 on 2024-03-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_remove_checkout_address_delete_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
