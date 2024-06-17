# Generated by Django 5.0.1 on 2024-02-09 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0013_alter_foods_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='categorymenu',
        ),
        migrations.AddField(
            model_name='foods',
            name='categorymenu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='res.categorymenu'),
        ),
    ]
