# Generated by Django 5.0.1 on 2024-02-09 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0027_remove_foodsingredient_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='res.foods'),
        ),
        migrations.DeleteModel(
            name='FoodsIngredient',
        ),
    ]
