# Generated by Django 4.2.3 on 2023-10-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_rename_subcategores_category_subcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(related_name='subcategory', to='shop.subcategory'),
        ),
    ]