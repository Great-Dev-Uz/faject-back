# Generated by Django 5.1 on 2024-08-21 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faject', '0002_subcategory_subcategorytranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faject.category', verbose_name='Категория'),
        ),
    ]