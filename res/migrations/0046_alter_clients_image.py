# Generated by Django 5.0.1 on 2024-03-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0045_clients_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
