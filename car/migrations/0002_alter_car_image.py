# Generated by Django 5.0.1 on 2024-02-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='car/media/uploads/'),
        ),
    ]
