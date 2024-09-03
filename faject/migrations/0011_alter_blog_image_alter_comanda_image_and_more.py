# Generated by Django 5.1 on 2024-09-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faject', '0010_projects_category_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(upload_to='blog/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='image',
            field=models.FileField(upload_to='comanda/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='howdowork',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='service/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FileField(upload_to='projects/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='tools',
            name='image',
            field=models.FileField(upload_to='tools', verbose_name='Изображение'),
        ),
    ]
