# Generated by Django 3.2.7 on 2021-09-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(default='', max_length=50)),
                ('sub_cat', models.CharField(default='', max_length=50)),
                ('p_name', models.CharField(default='', max_length=50)),
                ('p_date', models.DateField()),
                ('desc', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
