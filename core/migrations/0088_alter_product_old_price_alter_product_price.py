# Generated by Django 4.2.4 on 2024-02-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0087_remove_product_canonical_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="old_price",
            field=models.DecimalField(
                decimal_places=2, default="2", max_digits=99999999999
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default="1", max_digits=99999999999999
            ),
        ),
    ]
