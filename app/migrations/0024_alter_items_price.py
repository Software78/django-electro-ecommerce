# Generated by Django 3.2.4 on 2021-06-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
