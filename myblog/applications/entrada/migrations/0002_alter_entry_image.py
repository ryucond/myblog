# Generated by Django 4.1.4 on 2022-12-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Imagen'),
        ),
    ]
