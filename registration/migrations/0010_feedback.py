# Generated by Django 2.1.15 on 2022-04-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_companydetails_presentation_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('feedback', models.CharField(blank=True, max_length=5000, null=True)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(null=True)),
            ],
        ),
    ]