# Generated by Django 4.1 on 2022-09-13 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name_plural': 'tax'},
        ),
    ]