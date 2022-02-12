# Generated by Django 4.0.1 on 2022-02-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_brand_new1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='expiry_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Start Date'),
        ),
    ]
