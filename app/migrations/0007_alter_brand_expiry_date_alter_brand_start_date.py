# Generated by Django 4.0.1 on 2022-02-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_brand_expiry_date_alter_brand_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Start Date'),
        ),
    ]
