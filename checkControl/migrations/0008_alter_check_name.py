# Generated by Django 3.2 on 2022-12-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkControl', '0007_auto_20221212_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='name',
            field=models.CharField(max_length=30, verbose_name='表单名'),
        ),
    ]