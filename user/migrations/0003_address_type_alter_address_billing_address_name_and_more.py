# Generated by Django 5.0.7 on 2024-09-06 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address_billing_address_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('home', 'Home'), ('office', 'Office')], default='home', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='billing_address_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='billing_address_phone',
            field=models.CharField(default='N.A', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
