# Generated by Django 3.0.7 on 2020-06-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_color_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(help_text='Максимальная длина 254 символа', max_length=255, unique=True, verbose_name='Название'),
        ),
    ]
