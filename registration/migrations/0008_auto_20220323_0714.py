# Generated by Django 2.1.15 on 2022-03-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20220315_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessandcertification',
            name='certification_file',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='othercertification',
            name='certification_file',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='veteranownedbusiness',
            name='certification_file',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='womenownedbusiness',
            name='certification_file',
            field=models.CharField(default='', max_length=255),
        ),
    ]