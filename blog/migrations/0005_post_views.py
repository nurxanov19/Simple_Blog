# Generated by Django 5.1.7 on 2025-03-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_cateogry_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
