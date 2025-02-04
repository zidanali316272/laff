# Generated by Django 5.0.1 on 2024-02-09 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0024_remove_foodsingredient_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='foodsingredient',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='foodsingredient',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='res.foods'),
        ),
        migrations.AddField(
            model_name='foods',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='res.ingredient'),
        ),
        migrations.AddField(
            model_name='foodsingredient',
            name='ingredients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='res.ingredient'),
        ),
    ]
