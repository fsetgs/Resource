# Generated by Django 3.2 on 2022-11-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0006_auto_20221108_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='编码'),
        ),
        migrations.AddField(
            model_name='department',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='编码'),
        ),
    ]
