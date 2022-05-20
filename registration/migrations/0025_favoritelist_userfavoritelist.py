# Generated by Django 2.1.15 on 2022-05-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.BigIntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=1055, null=True)),
                ('category', models.CharField(blank=True, max_length=1055, null=True)),
                ('location', models.CharField(blank=True, max_length=1055, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abc_corporation_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
