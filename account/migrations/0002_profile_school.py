# Generated by Django 3.0.7 on 2020-07-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
