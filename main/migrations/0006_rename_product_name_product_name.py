# Generated by Django 3.2.4 on 2021-12-27 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_categories_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]