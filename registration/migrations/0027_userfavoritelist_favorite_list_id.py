# Generated by Django 2.1.15 on 2022-05-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0026_auto_20220519_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfavoritelist',
            name='favorite_list_id',
            field=models.IntegerField(default=0),
        ),
    ]