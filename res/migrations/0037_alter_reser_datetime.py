# Generated by Django 5.0.1 on 2024-02-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0036_alter_reser_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reser',
            name='datetime',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
