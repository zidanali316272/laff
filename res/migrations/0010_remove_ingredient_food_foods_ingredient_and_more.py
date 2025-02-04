# Generated by Django 5.0.1 on 2024-02-04 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0009_remove_ingredient_food_ingredient_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='food',
        ),
        migrations.AddField(
            model_name='foods',
            name='ingredient',
            field=models.ManyToManyField(to='res.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
    ]
