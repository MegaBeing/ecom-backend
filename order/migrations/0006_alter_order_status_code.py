# Generated by Django 5.0.7 on 2024-08-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_status_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_code',
            field=models.IntegerField(choices=[(0, 'Ordered'), (6, 'Shipped'), (7, 'Delivered'), (8, 'Canceled'), (17, 'Out for delivery'), (18, 'In transit')]),
        ),
    ]
