# Generated by Django 4.2.7 on 2023-12-17 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comments',
        ),
    ]