# Generated by Django 3.2 on 2022-12-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataControl', '0010_resource_duty'),
    ]

    operations = [
        migrations.CreateModel(
            name='resourceName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, verbose_name='资产名称')),
            ],
        ),
    ]
