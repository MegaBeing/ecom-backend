# Generated by Django 5.0.7 on 2024-08-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_id', models.CharField(max_length=50)),
                ('order_id', models.CharField(max_length=50)),
                ('status_code', models.PositiveIntegerField(choices=[(0, 'Ordered'), (6, 'Shipped'), (7, 'Delivered'), (8, 'Canceled'), (17, 'Out for delivery'), (18, 'In transit')])),
                ('payment_status', models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'Pending')], default='pending', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
