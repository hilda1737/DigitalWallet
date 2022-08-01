# Generated by Django 4.0.6 on 2022-07-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=8, null=True)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptdate', models.DateTimeField()),
                ('file', models.FileField(max_length=15, upload_to='')),
            ],
        ),
    ]