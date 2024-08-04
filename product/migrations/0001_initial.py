# Generated by Django 5.0.7 on 2024-08-03 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Clutch bag', 'Clutch bag'), ('Potlis', 'Potlis'), ('Batua bag', 'Batua bag'), ('Bridal bag', 'Bridal bag')], default='Clutch bag', max_length=50)),
            ],
            options={
                'verbose_name': 'Product Cluster',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=None)),
                ('product', models.ManyToManyField(to='product.productcluster')),
            ],
        ),
        migrations.CreateModel(
            name='SingleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=500)),
                ('previous_price', models.PositiveIntegerField(blank=True, null=True)),
                ('length', models.FloatField()),
                ('breath', models.FloatField()),
                ('height', models.FloatField()),
                ('color', models.CharField(max_length=10)),
                ('in_stock', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.productcluster')),
            ],
            options={
                'verbose_name': 'Single Product',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('alt_text', models.CharField(blank=True, max_length=100)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.singleproduct')),
            ],
        ),
    ]
