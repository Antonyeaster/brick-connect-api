# Generated by Django 3.2.24 on 2024-03-04 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='posts.post'),
        ),
    ]