# Generated by Django 4.1 on 2022-09-11 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_openinghour'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='openinghour',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]