# Generated by Django 4.1.3 on 2022-11-23 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 14, 58, 57, 945112, tzinfo=datetime.timezone.utc), verbose_name='Posted on'),
        ),
    ]
