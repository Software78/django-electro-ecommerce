# Generated by Django 3.2.4 on 2021-06-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_categories_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.IntegerField(choices=[(1, 'Phones'), (2, 'Laptops'), (3, 'Batteries'), (4, 'Chargers')], default=1),
        ),
    ]
