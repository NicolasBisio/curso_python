# Generated by Django 4.2.7 on 2023-11-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ecommerce', '0003_rename_user_cart_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
