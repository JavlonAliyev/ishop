# Generated by Django 4.0.1 on 2022-01-20 03:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_image_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]