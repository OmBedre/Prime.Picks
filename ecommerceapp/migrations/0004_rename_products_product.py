# Generated by Django 5.0.6 on 2024-07-09 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_products'),  # Dependency on the previous migration
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',  # Old model name to be renamed
            new_name='Product',   # New model name
        ),
    ]
