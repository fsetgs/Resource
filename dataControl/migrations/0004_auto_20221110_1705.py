# Generated by Django 3.2 on 2022-11-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataControl', '0003_auto_20221109_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceinfo',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='resourceinfo',
            name='month_depreciation',
        ),
        migrations.RemoveField(
            model_name='resourceinfo',
            name='net_assets',
        ),
        migrations.RemoveField(
            model_name='resourceinfo',
            name='total_depreciation',
        ),
        migrations.AddField(
            model_name='resource',
            name='code',
            field=models.CharField(default='0', max_length=20, verbose_name='资产编码'),
        ),
        migrations.AddField(
            model_name='resourceinfo',
            name='product',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='制造商'),
        ),
    ]
