# Generated by Django 3.2.7 on 2021-09-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0010_auto_20210925_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Sports', 'Sports'), ('Home & Furniture', 'Home & Furniture'), ('Boooks', 'Books'), ('Health & Nutritions', 'Health & Nutritions')], default='1', max_length=50),
        ),
    ]
