# Generated by Django 3.2.7 on 2021-09-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Eectronics', 'Eectronics'), ('Tea', 'Tea'), ('Fruits', 'Fruits'), ('Vegetables', 'Vegetables'), ('Chicken', 'Chicken'), ('Games', 'Games')], default='1', max_length=50),
        ),
    ]
