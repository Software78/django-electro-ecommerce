# Generated by Django 3.2.4 on 2021-06-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_phones_new_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='discount',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
