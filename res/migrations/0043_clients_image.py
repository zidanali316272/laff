# Generated by Django 5.0.1 on 2024-03-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0042_remove_clients_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
