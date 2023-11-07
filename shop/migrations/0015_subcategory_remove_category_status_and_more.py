# Generated by Django 4.2.3 on 2023-10-20 14:20

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_is_exclusive'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='1-show, 0-hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default, 1-trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='category',
            name='trending',
        ),
        migrations.AddField(
            model_name='category',
            name='subcategores',
            field=models.ManyToManyField(related_name='categories', to='shop.subcategory'),
        ),
    ]