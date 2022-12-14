# Generated by Django 3.2 on 2022-11-03 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='公司名称')),
                ('comment', models.CharField(max_length=50, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='部门名称')),
                ('comment', models.CharField(max_length=50, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=20, verbose_name='真实姓名')),
                ('username', models.CharField(max_length=200, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userControl.company', verbose_name='所属公司')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userControl.department', verbose_name='所属部门')),
            ],
        ),
    ]
