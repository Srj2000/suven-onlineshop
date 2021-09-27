# Generated by Django 3.2.7 on 2021-09-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0009_auto_20210924_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fashiom', 'Fashion'), ('Sports', 'Sports'), ('Home & Furniture', 'Home & Furniture'), ('Boooks', 'Books'), ('Health & Nutritions', 'Health & Nutritions')], default='1', max_length=50),
        ),
    ]
