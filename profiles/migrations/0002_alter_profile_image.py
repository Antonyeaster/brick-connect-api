# Generated by Django 3.2.24 on 2024-02-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_reihu8', upload_to='images/'),
        ),
    ]
