# Generated by Django 4.0.5 on 2022-06-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecurityApp', '0005_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(),
        ),
    ]