# Generated by Django 4.0.1 on 2022-02-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_brand_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='new1',
            field=models.DateField(blank=True, null=True, verbose_name='new1'),
        ),
    ]