# Generated by Django 3.2.7 on 2021-09-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_gamegroup'),
        ('accounts', '0007_auto_20210926_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='main.GameGroup'),
        ),
        migrations.DeleteModel(
            name='GameGroup',
        ),
    ]
