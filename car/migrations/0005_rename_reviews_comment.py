# Generated by Django 5.0.1 on 2024-02-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_rename_cars_reviews_car'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reviews',
            new_name='Comment',
        ),
    ]