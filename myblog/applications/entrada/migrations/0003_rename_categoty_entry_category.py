# Generated by Django 4.1.4 on 2022-12-31 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0002_alter_entry_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='categoty',
            new_name='category',
        ),
    ]
