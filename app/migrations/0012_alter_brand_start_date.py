# Generated by Django 4.0.1 on 2022-05-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_brand_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Start Date'),
        ),
    ]
