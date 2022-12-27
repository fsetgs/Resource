# Generated by Django 3.2 on 2022-11-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataControl', '0006_alter_resource_resource_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='resourceinfo',
            name='level',
        ),
        migrations.RemoveField(
            model_name='resourceinfo',
            name='product',
        ),
        migrations.AddField(
            model_name='resourceinfo',
            name='mac',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='MAC'),
        ),
        migrations.AddField(
            model_name='resourceinfo',
            name='month_depreciation',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='月折旧额'),
        ),
        migrations.AddField(
            model_name='resourceinfo',
            name='net_value',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='资产净值'),
        ),
        migrations.AddField(
            model_name='resourceinfo',
            name='total_depreciation',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='累计折旧'),
        ),
    ]