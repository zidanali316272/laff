# Generated by Django 5.0.1 on 2024-02-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0032_alter_reser_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reser',
            name='datetime',
            field=models.TextField(null=True),
        ),
    ]
