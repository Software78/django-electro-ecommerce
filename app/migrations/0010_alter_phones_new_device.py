# Generated by Django 3.2.4 on 2021-06-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_phones_new_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='new_device',
            field=models.BooleanField(default=False),
        ),
    ]
