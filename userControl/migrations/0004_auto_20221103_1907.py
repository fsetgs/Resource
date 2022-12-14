# Generated by Django 3.2 on 2022-11-03 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userControl', '0003_alter_userinfo_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userControl.company', verbose_name='所属公司'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userControl.department', verbose_name='所属部门'),
        ),
    ]
