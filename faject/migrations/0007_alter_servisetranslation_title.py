# Generated by Django 5.1 on 2024-08-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faject', '0006_alter_servisetranslation_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servisetranslation',
            name='title',
            field=models.CharField(max_length=250, verbose_name='title'),
        ),
    ]
