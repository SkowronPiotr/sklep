# Generated by Django 4.2.5 on 2023-10-17 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='conversdation',
            new_name='conversation',
        ),
    ]
