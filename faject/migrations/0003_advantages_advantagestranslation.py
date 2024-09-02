# Generated by Django 5.1 on 2024-09-02 06:13

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faject', '0002_servise_icon_servisetranslation_short_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='faject.servise', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'ПРЕИМУЩЕСТВА',
                'verbose_name_plural': 'ПРЕИМУЩЕСТВА',
                'ordering': ['id'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AdvantagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Описание')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='faject.advantages')),
            ],
            options={
                'verbose_name': 'ПРЕИМУЩЕСТВА Translation',
                'db_table': 'faject_advantages_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
