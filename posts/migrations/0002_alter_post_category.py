# Generated by Django 3.2.24 on 2024-03-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('full set builds', 'Full Sets Builds'), ('diy builds', 'Diy Builds')], default='full set builds', max_length=100),
        ),
    ]