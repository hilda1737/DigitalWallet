# Generated by Django 4.0.6 on 2022-08-23 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Adress',
            new_name='address',
        ),
    ]
