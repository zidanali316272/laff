# Generated by Django 5.0.1 on 2024-02-09 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0022_ingredient_remove_foods_ingredients_foods_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodsIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.ingredient')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.foods')),
            ],
        ),
    ]
