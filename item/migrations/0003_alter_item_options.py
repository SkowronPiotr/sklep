# Generated by Django 4.2.5 on 2023-10-05 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Przedmioty'},
        ),
    ]
