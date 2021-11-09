# Generated by Django 3.2.9 on 2021-11-09 12:30

from django.db import migrations, models

import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_auto_20211029_2330"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="address2",
            field=models.TextField(
                blank=True,
                null=True,
                validators=[accounts.models.validate_address],
                verbose_name="address 2",
            ),
        ),
    ]
