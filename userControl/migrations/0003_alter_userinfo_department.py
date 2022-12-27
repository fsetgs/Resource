# Generated by Django 3.2 on 2022-11-03 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0002_alter_userinfo_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userControl.department', verbose_name='所属部门'),
        ),
    ]
