# Generated by Django 5.0.1 on 2024-02-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0039_clients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='Profession',
            new_name='profession',
        ),
    ]
