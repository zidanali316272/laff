# Generated by Django 5.0.1 on 2024-06-04 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0051_reser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reser',
            name='user',
        ),
    ]
