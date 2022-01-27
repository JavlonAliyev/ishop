# Generated by Django 4.0.1 on 2022-01-27 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_alter_country_options_rename_name_ru_country_name_en_and_more'),
        ('main', '0003_product_added_at_product_available_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='common.country')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='common.district')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='common.region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.BigIntegerField()),
                ('order_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cart.deliveryaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(default=0)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cart.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.product')),
            ],
        ),
    ]
